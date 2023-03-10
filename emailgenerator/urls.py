from django.urls import path
from emailgenerator.views import EmailGenerator

app_name = 'emailgenerator'

urlpatterns = [
    path('', EmailGenerator.as_view(), name='emailgenerator'),
]