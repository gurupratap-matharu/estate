from django.urls import path

from market.views import HomePageView

app_name = 'market'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
