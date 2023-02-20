from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class CbvContext(TemplateView):
    template_name='CbvContext.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='ASHU'
        context['age']=3
        return context