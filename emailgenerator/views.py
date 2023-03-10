from django.shortcuts import render
from django.views.generic import TemplateView

class EmailGenerator(TemplateView):
    template_name = 'emailgenerator/index.html'