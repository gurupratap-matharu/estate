from django.test import TestCase
from django.urls import resolve, reverse
from market.views import HomePageView, SearchResultsView


class HomePageTests(TestCase):
    def test_home_page_works(self):
        response = self.client.get(reverse('market:home'))
        no_response = self.client.get('/home/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market/home.html')
        self.assertContains(response, 'Home')
        self.assertNotContains(response, 'Hi I should not be on this page!')
        self.assertEqual(no_response.status_code, 404)

    def test_home_page_resolve_homepageview(self):
        view = resolve(reverse('market:home'))
        self.assertEqual(view.func.__name__, HomePageView.__name__)
