from django.urls import path

from market.views import HomePageView, SearchResultsView

app_name = 'market'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
]
