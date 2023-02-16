from django.views.generic import TemplateView, ListView
from blog.models import Post,Category
from api.utils import obj_to_post
import json

# class HomeView(TemplateView):
#     template_name = 'home.html'

class HomeView(ListView):
    # model = Post
    template_name = 'home.html'
    paginate_by = 3

    def get_queryset(self):
        paramCate = self.request.GET.get('category')
        if paramCate:
            qs = Post.objects.filter(category__name__iexact=paramCate)
        else:
            qs = Post.objects.all()
        return qs
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        postList = [obj_to_post(obj) for obj in context['object_list']]
        pageCnt = context['paginator'].num_pages
        curPage = context['page_obj'].number

        qs1 = Category.objects.all()
        cateList = [cate.name for cate in qs1]

        dataDict = {
            'postList': postList,
            'pageCnt': pageCnt,
            'curPage': curPage,
            'cateList': cateList,
        }
        context['myJson'] = json.dumps(dataDict)
        return context