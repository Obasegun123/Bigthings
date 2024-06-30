
import django.dispatch
from django.dispatch import receiver

from .models import AuditTrail
import logging
import datetime


audit_trail_signal = django.dispatch.Signal(providing_args=['user', 'request', 'model', 'event_category', 'method', 'summary']) # creates a custom signal and specifies the args required. 

logger = logging.getLogger(__name__)

#helper func that gets the client ip
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@receiver(audit_trail_signal)
def log_audit_trail(sender, user, request, model, event_category, method,summary,**kwargs):
    try:

        user_agent_info = request.META.get('HTTP_USER_AGENT', '<unknown>')[:255],
        print(summary)
        auditTrail = AuditTrail.objects.create( 
            user=user,
            user_agent_info=user_agent_info,
            changed_object = model ,
            event_category = event_category ,
            login_IP = get_client_ip(request),
            is_deleted = False,
            action=method,
            change_summary=summary
        )
        logger.info(f"Audit trail created {auditTrail.id}  for user {auditTrail.username} and object {auditTrail.changed_object}")
    except Exception as e:

        logger.error("log_user_logged_in request: %s, error: %s" % (request, e))
