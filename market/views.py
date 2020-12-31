from django.views.generic import ListView, TemplateView

from market.models import Apartment, House


class HomePageView(TemplateView):
    template_name = 'market/home.html'


class SearchResultsView(TemplateView):
    template_name = 'market/search_results.html'


class ProperyListView(ListView):
    model = None
    template_name = 'market/property_list.html'
    paginate_by = 9
    context_object_name = 'property_list'


class HouseListView(ProperyListView):
    model = House


class ApartmentListView(ProperyListView):
    model = Apartment
