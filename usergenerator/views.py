from django.views.generic import TemplateView


class UserGenerator(TemplateView):
    template_name = 'usergenerator/index.html'