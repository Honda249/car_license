from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'base/index.html'  # Specify the template you want to render

    # Optionally, you can override the get_context_data method to pass context to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'  # Example of adding a variable to the context
        return context

