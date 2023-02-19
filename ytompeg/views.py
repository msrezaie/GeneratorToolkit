from django.views.generic import TemplateView


class YouTubeToMpeg(TemplateView):
    template_name = 'ytompeg/index.html'