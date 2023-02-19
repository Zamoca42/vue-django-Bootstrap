# from rest_framework import viewsets
# from django.contrib.auth.models import User

# from api2.serializers import UserSerializer, PostSerializer
# from blog.models import Post

# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
# --------------------------------------------

# generic view

from api2.serializers import PostListSerializer, PostRetrieveSerializer, CateTagSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from blog.models import Post, Category, Tag
from rest_framework.response import Response
from rest_framework.views import APIView

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveSerializer

# class PostLikeAPIView(UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostLikeSerializer
    
#     # PATCH Method
#     def update(self, request, *args, **kwargs):
#       partial = kwargs.pop('partial', False)
#       instance = self.get_object()
#     #   data = instance.like + 1
#       data = {'like': instance.like + 1}
#       serializer = self.get_serializer(instance, data=data, partial=partial)
#       serializer.is_valid(raise_exception=True)
#       self.perform_update(serializer)

#       if getattr(instance, '_prefetched_objects_cache', None):
#           # If 'prefetch_related' has been applied to a queryset, we need to
#           # forcibly invalidate the prefetch cache on the instance.
#           instance._prefetched_objects_cache = {}

#       return Response(data['like'])

class CateTagAPIView(APIView):
    def get(self, request, *args, **kwargs):
        cateList = Category.objects.all()
        tagList = Tag.objects.all()
        data = {
            'cateList': cateList,
            'tagList': tagList,
        }

        serializer = CateTagSerializer(instance=data)
        return Response(serializer.data)

class PostLikeAPIView(GenericAPIView):
    queryset = Post.objects.all()
    # serializer_class = PostLikeSerializer
    
    # PATCH Method
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()

        return Response(instance.like)