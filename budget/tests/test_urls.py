from django.test import SimpleTestCase
from django.urls import resolve, reverse
from budget.views import project_list, ProjectCreateView, project_detail


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolves(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, project_list)

    def test_create_project_url_is_resolves(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, project_detail)
