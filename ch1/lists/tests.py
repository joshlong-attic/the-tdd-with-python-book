from django.http import HttpRequest
from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self) -> None:
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_root_url_resolves_to_home_page_view(self) -> None:
        found = resolve('/')
        self.assertEquals(found.func, home_page)
