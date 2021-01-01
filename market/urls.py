from django.urls import path

from market.views import (ApartmentDetailView, ApartmentListView, HomePageView,
                          HouseDetailView, HouseListView, SearchResultsView)

app_name = 'market'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('house/', HouseListView.as_view(), name='house_list'),
    path('house/<uuid:pk>/', HouseDetailView.as_view(), name='house_detail'),
    path('apartment/', ApartmentListView.as_view(), name='apartment_list'),
    path('apartment/<uuid:pk>/', ApartmentDetailView.as_view(), name='apartment_detail'),
]
