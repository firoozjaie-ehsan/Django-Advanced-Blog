from django.urls import path, include
from .views import IndexView, ArticleListView, post_Detail_view,PostsEditView,PostsCreateView, PostDeleteView, Post_ListView

app_name = "blog"

urlpatterns = [
    # path("", indexView, name="funtion_test"),
    path("index/", IndexView.as_view()),
    path("posts/",  ArticleListView.as_view(), name="post_list"),
    path("post/<int:pk>/", post_Detail_view.as_view(), name="post-detail"),
    path("post/create/", PostsCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit", PostsEditView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls"))
    
]