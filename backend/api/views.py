from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.views import View

from api.utils import obj_to_post, prev_next_post
from blog.models import Post, Category

class ApiPostLV(BaseListView):
    #model = Post
    paginate_by = 3

    def get_queryset(self):
        paramCate = self.request.GET.get('category')
        if paramCate:
            qs = Post.objects.filter(category__name__iexact=paramCate)
        else:
            qs = Post.objects.all()
        return qs

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        postList = [obj_to_post(obj, False) for obj in qs]

        pageCnt = context['paginator'].num_pages
        curPage = context['page_obj'].number

        jsonData = {
            'postList': postList,
            'pageCnt': pageCnt,
            'curPage': curPage,
        }
        return JsonResponse(data=jsonData, safe=True, status=200)


class ApiPostDV(BaseDetailView):
    # model = Post

    def get_queryset(self):
        return post.objects.all().select_related('category')

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)

        jsonData = {
            'post': post,
            'prevPost': prevPost,
            'nextPost': nextPost,
        }
        return JsonResponse(data=jsonData, safe=True, status=200)

class ApiCateTagView(View):
    def get(self, request, *args, **kwargs):
        qs1 = Category.objects.all()

        cateList = [cate.name for cate in qs1]

        jsonData = {
            'cateList': cateList,
        }
    
        return JsonResponse(data=jsonData, safe=True, status=200)


