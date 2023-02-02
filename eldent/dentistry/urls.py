from django.urls import path

from . import views

app_name = 'dentistry'
urlpatterns = [
    path('', views.index, name='index'),
]