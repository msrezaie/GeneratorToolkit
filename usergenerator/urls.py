from django.urls import path
from usergenerator.views import UserGenerator

app_name = 'usergenerator'

urlpatterns = [
    path('', UserGenerator.as_view(), name='usergenerator'),
]