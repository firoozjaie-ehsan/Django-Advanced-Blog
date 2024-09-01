from datetime import datetime
from django.test import TestCase,Client
from django.urls import reverse
from accounts.models import User, Profile
from blog.models import Post, Category

class TestBlogView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="admin@admin.com", password="Ee@9117409534"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test first name",
            last_name="test last name",
            description="test description",
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="test",
            content="description",
            category=None,
            status=True,
            published_date=datetime.now(),
        )
    def test_blog_index_url_successfully_response(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(bool(str(response.content).find("Ehsan")))
        self.assertTemplateUsed(response,"index.html")
        
    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse("blog:post-detail", kwargs=
                      {"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_blog_post_detail_anonymous_response(self):
        url = reverse("blog:post-detail", kwargs=
                      {"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        