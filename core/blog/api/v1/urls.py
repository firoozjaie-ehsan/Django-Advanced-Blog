from django.urls import path, include
from .views import PostList,PostDetail, PostList
from . import views
app_name = "api-v1"

urlpatterns = [
    # path("post/", PostList, name="post-list"),
    # path("post/<int:id>/", PostDetail, name="post-detail"),
    # path('post/', views.PostList.as_view(), name="post-list"),
    # path("post/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
    path("post/", views.PostViewSet.as_view({'get':'list', 'post':'create'}), name="post-list"),
    path("post/<int:pk>/", views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="post-detail"),
]