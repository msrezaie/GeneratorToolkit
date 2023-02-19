from django.urls import path
from ytompeg.views import YouTubeToMpeg

app_name = 'ytompeg'

urlpatterns = [
    path('', YouTubeToMpeg.as_view(), name='ytompeg'),
]