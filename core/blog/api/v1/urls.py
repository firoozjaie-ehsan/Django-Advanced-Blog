from django.urls import path, include
from .views import PostList,PostDetail, PostList
from . import views
app_name = "api-v1"

urlpatterns = [
    # path("post/", PostList, name="post-list"),
    # path("post/<int:id>/", PostDetail, name="post-detail"),
    
    path('post/', views.PostList.as_view(), name="post-list"),
    path("post/<int:id>/", views.PostDetail.as_view(), name="post-detail"),
    
    
]