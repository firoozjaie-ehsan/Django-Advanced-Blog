from django.views.generic import TemplateView, DetailView
from .models import Post
from django.views.generic.list import ListView
from rest_framework.decorators import api_view
from .forms import PostForm
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from rest_framework.response import Response

# Create your views here.

# def indexView(request):
#     return render(request,'index.html')


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(request, **kwargs):
        context = super().get_context_data(**kwargs)
        name = "Ehsan"
        context["name"] = name
        context["posts"] = Post.objects.all()
        return context


class ArticleListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    model = Post
    # queryset = Post.objects.filter(status=True).order_by('-created_at')
    context_object_name = "posts"
    # paginate_by = 2
    ordering = "-id"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class post_Detail_view(LoginRequiredMixin, DetailView):
    model = Post


"""
class PostsCreateView(FormView):
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/posts/"

    def get_template_names(self):
        template = get_template(self.template_name)
        print("Template found at:", template.origin)
        return [self.template_name]
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    """


class PostsCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # fields = ['author', 'title','content', 'category', 'status', 'published_date']
    success_url = "/blog/posts/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostsEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/posts/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/posts/"


@api_view(["GET"])
def Post_ListView(request):
    return Response({"name": "Ehsan"})
