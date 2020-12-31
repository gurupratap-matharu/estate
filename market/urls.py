from django.urls import path

from market.views import (ApartmentListView, HomePageView, HouseListView,
                          SearchResultsView)

app_name = 'market'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('house/', HouseListView.as_view(), name='house_list'),
    path('apartment/', ApartmentListView.as_view(), name='apartment_list'),
]
