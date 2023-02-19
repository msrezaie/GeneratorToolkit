from django.urls import path
from base.views import Base

app_name = 'base'

urlpatterns = [
    path('', Base.as_view(), name='base'),
]