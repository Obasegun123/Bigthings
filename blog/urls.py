from django.urls import path
from blog import views


urlpatterns = [
    path("v1/posts/", views.PostAPI.as_view(), name="get_a_list_of_all_blogs"),
    path("v1/tags/", views.TagAPI.as_view(), name="get_all_tags"),
    path("v1/posts/<str:id>/", views.PostDetailAPI.as_view(), name="get_a_post_detail"),
    
    path('audit-trail/', views.AuditTrailView.as_view(), name="audit_trail"),
]