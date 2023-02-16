from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from blog.models import Post, Category
from api.utils import obj_to_post, prev_next_post

import json
# Create your views here.

# class PostLV(ListView):
#     model = Post
#     # template_name = 'blog/post_list.html'

# class PostDV(TemplateView):
#     template_name = 'blog/post_detail.html'

class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        obj = context['object']
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)

        dataDict = {
            'post': post,
            'prevPost': prevPost,
            'nextPost': nextPost,
        }

        context['myJson'] = json.dumps(dataDict)
        return context