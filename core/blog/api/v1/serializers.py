from rest_framework import serializers
from ...models import Category, Post

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)
    
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = "__all__"
        fields = ['id', 'author', 'title','content', 'category', 'status', 'published_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']