from django.urls import path

from . import views

app_name = 'dentistry'
urlpatterns = [
    path('dent', views.index, name='index'),
]