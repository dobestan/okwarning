from django.views.generic import ListView

from proxy.models import Provider


class HomeView(ListView):
    model = Provider
    template_name = 'home.html'

    context_object_name = 'providers'
