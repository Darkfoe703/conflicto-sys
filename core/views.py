from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

""" class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

class ContactView(TemplateView):
    template_name = 'contact.html' """