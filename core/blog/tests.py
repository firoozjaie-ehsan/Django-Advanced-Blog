from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import ArticleListView

# Create your tests here.


class TestUrl(SimpleTestCase):

    def test_blog_index_url_resolve(self):
        url = reverse("blog:post_list")
        self.assertEquals(resolve(url).func.view_class, ArticleListView)
