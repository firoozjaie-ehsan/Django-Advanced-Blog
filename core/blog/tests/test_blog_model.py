from django.test import TestCase
from datetime import datetime
from ..models import Post, Category
from django.contrib.auth import get_user_model
from accounts.models import User, Profile


class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="admin@admin.com", password="Ee@9117409534"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test first name",
            last_name="test last name",
            description="test description",
        )

    def test_post_form_with_valid_data(self):

        post = Post.objects.create(
            author=self.profile,
            title="Test",
            content="description",
            category=None,
            status=True,
            published_date=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEqual(post.title, "Test")
