from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pegination import DefaultPagination

# create function based view
"""
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def PostList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def PostDetail(request, id):
    post = get_object_or_404(Post,pk=id, status = True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method =="PUT":
        serializer = PostSerializer(post, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method =="DELETE":
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
        """

# example for class based rest views
'''
class PostList(APIView):
    """getting a list of posts and creating new post"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request):
        """retrieves a list of posts"""
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request):
        """creates a new post with provided data"""
        serializer = PostSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        '''


'''
class PostDetail(APIView):
    """getting a post, updating it and deleting it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request , id):
        """retrieves a single post"""
        post = get_object_or_404(Post,pk=id, status = True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request , id):
        """updates a single post"""
        post = get_object_or_404(Post,pk=id, status = True)
        serializer = PostSerializer(post, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        """delete a single post"""
        post = get_object_or_404(Post,pk=id, status = True)
        post.delete()
        return Response({"detail":"Item removed successfully"},status=status.HTTP_204_NO_CONTENT)
    '''

# Example for GenericAPIView for class based views
# class PostList(ListCreateAPIView):
#     """getting a list of posts and creating new post"""
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     """getting a post, updating it and deleting it"""
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)


# Example for viewSet in CBV
class PostModelViewSet(viewsets.ModelViewSet):
    """getting a list of posts and creating new post"""

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
