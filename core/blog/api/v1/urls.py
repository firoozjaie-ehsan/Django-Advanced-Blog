from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"
router = DefaultRouter()
router.register(r"post", views.PostModelViewSet, basename="post")
router.register(r"category", views.CategoryModelViewSet, basename="category")
urlpatterns = router.urls

# urlpatterns = [
#     # path("post/", PostList, name="post-list"),
#     # path("post/<int:id>/", PostDetail, name="post-detail"),
#     # path('post/', views.PostList.as_view(), name="post-list"),
#     # path("post/<int:pk>/", views.PostDetail.as_view(), name="post-detail"),
#     path("post/", views.PostViewSet.as_view({'get':'list', 'post':'create'}), name="post-list"),
#     path("post/<int:pk>/", views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="post-detail"),
# ]
