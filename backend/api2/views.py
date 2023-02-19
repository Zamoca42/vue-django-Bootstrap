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

# from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from api2.serializers import PostListSerializer, PostRetrieveSerializer, CateTagSerializer, PostSerializerDetail 
from rest_framework.pagination import PageNumberPagination
from blog.models import Post, Category, Tag
from rest_framework.response import Response
from rest_framework.views import APIView
from collections import OrderedDict
from rest_framework.viewsets import ModelViewSet

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

# class PostLikeAPIView(GenericAPIView):
#     queryset = Post.objects.all()
    
#     def get(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.like += 1
#         instance.save()

#         return Response(instance.like)

class PostPageNumberPagination(PageNumberPagination):
    page_size = 3
    def get_paginated_response(self, data):
      return Response(OrderedDict([
          ('postList', data),
          ('pageCnt', self.page.paginator.num_pages),
          ('curPage', self.page.number),
      ]))

# class PostListAPIView(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostListSerializer
#     pagination_class = PostPageNumberPagination

#     def get_serializer_context(self):

#       return {
#           'request': None,
#           'format': self.format_kwarg,
#           'view': self
#       }

# def get_prev_next(instance):
#     try:
#         prev = instance.get_previous_by_modify_dt()
#     except instance.DoesNotExist:
#         prev = None
    
#     try:
#         next_ = instance.get_next_by_modify_dt()
#     except instance.DoesNotExist:
#         next_ = None
    
#     return prev, next_

# class PostRetrieveAPIView(RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializerDetail

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         prevInstance, nextInstance = get_prev_next(instance)
#         data = {
#             'post': instance,
#             'prevPost': prevInstance,
#             'nextPost': nextInstance,
#         }
#         serializer = self.get_serializer(instance=data)
#         return Response(serializer.data)
    
#     def get_serializer_context(self):

#       return {
#           'request': None,
#           'format': self.format_kwarg,
#           'view': self
#       }

def get_prev_next(instance):
        try:
            prev = instance.get_previous_by_modify_dt()
        except instance.DoesNotExist:
            prev = None

        try:
            next_ = instance.get_next_by_modify_dt()
        except instance.DoesNotExist:
            next_ = None

        return prev, next_

class PostViewSet(ModelViewSet):
    pagination_class = PostPageNumberPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        if self.action == 'retrieve':
            return PostSerializerDetail
        return PostSerializerDetail
   
    def get_queryset(self):
        return Post.objects.all().select_related('category').prefetch_related('tags')
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        prevInstance, nextInstance = get_prev_next(instance)
        data = {
            'post': instance,
            'prevPost': prevInstance,
            'nextPost': nextInstance,
        }
        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)
    
    def get_serializer_context(self):

      return {
          'request': None,
          'format': self.format_kwarg,
          'view': self
      }

    def like(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()

        return Response(instance.like)
    
    