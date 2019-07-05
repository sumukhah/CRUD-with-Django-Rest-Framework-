from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Post.views import PostListView, PostDetailView, CommentView


class Test(SimpleTestCase):

    def test_list_url_is_resolves(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_detail_url_resolves(self):
        url = reverse('detail')
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_comment_url_resolves(self):
        url = reverse('comments')
        self.assertEquals(resolve(url).func.view_class, CommentView)
