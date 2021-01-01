from django.views.generic import DetailView, ListView, TemplateView

from market.models import Apartment, House


class HomePageView(TemplateView):
    template_name = 'market/home.html'


class PropertyListView(ListView):
    model = None
    template_name = 'market/property_list.html'
    context_object_name = 'property_list'


class PropertyDetailView(DetailView):
    model = None
    template_name = 'market/property_detail.html'
    context_object_name = 'property'


class HouseListView(PropertyListView):
    model = House


class HouseDetailView(PropertyDetailView):
    model = House


class ApartmentListView(PropertyListView):
    model = Apartment


class ApartmentDetailView(PropertyDetailView):
    model = Apartment
