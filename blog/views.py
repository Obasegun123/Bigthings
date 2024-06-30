from rest_framework import permissions, status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


import requests
# Create your views here.

from .models import Post, Tag, AuditTrail
from blog.serializers import TagSerializer, PostDetailSerializer, PostSerializer,AuditTrailSerializer


class TagAPI(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all().order_by("-created_at")
    permission_classes = [permissions.IsAuthenticated]


class PostAPI(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-created_at")
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        data = self.request.data
        new_post = serializer.save(
            user=self.request.user, title=data["title"], content=data["content"]
        )
        all_posts = Post.objects.all().order_by("-created_at")
        serializer = PostSerializer(all_posts, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




# class PostDetailAPI(APIView):
#     def get(self, request, id):
#         post = get_post(id)
#         serializer = PostDetailSerializer(post)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

class PostDetailAPI(APIView):
    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)  # Use pk (primary key) for id
        serializer = PostDetailSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostAPI(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by("-created_at")
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        data = self.request.data
        new_post = serializer.save(
            user=self.request.user, title=data["title"], content=data["content"]
        )
        all_posts = Post.objects.all().order_by("-created_at")
        serializer = PostSerializer(all_posts, many=True)
        audit_trail_signal.send(sender=request.user.__class__, request=request, 
        user=request.user, model="Blog",event_category="Blog", method="CREATE")
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AuditTrailView(generics.ListAPIView):
    authentication_classes = ( permissions.IsAuthenticated,)
    queryset = AuditTrail.objects.all().order_by('-created')
    serializer_class = AuditTrailSerializer
    permission_classes = ( permissions.IsAuthenticated,)