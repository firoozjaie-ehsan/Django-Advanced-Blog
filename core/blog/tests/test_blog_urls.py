from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import ArticleListView, post_Detail_view

# Create your tests here.


class TestUrl(SimpleTestCase):

    def test_blog_list_url_resolve(self):
        url = reverse("blog:post_list")
        self.assertEquals(resolve(url).func.view_class, ArticleListView)

    def test_blog_detail_url_resolve(self):
        url = reverse("blog:post-detail", kwargs={"pk": 8})
        self.assertEquals(resolve(url).func.view_class, post_Detail_view)
