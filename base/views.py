from django.views.generic import TemplateView
from . models import App


class Base(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apps = App.objects.all()
        context['apps'] = apps
        return context