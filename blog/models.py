# Create your models here.

from django.db import models
from django.contrib.auth import get_user_model

import uuid


# Create your models here.


User = get_user_model()

class TimeStampedUUIDModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampedUUIDModel):
    title = models.CharField(max_length=199)

    def __str__(self) -> str:
        return self.title


class Post(TimeStampedUUIDModel):
    user = models.ForeignKey(User, related_name="posts",
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=199)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    isPublished = models.BooleanField(default=False)
    image = models.CharField(max_length=255, null=True)
    slug = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.title


class AuditTrail(TimeStampedUUIDModel):
    login_IP = models.GenericIPAddressField(null=True, blank=True)
    action_datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # keeps track of the user 
    changed_object = models.CharField(max_length=40)
    event_category = models.CharField(max_length=40)
    user_agent_info = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)
    action = models.CharField(max_length=40)
    change_summary = models.CharField(max_length=199)
