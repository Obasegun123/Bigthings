from rest_framework import serializers
from blog.models import Post, Tag, AuditTrail


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields =  (
            "id",
            "title",
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
        )


class PostDetailSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "title", "content", "tags")

    def get_tags(self, obj):
        return TagSerializer(obj.tags.all(), many=True).data
    
    
class AuditTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditTrail
        fields = ( 
            "id",
            "action_datetime",
            "user",
            "changed_object",
            "event_category",
            "change_summary",
        )

