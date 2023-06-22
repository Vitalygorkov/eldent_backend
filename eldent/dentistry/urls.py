from django.urls import path

from . import views

app_name = 'dentistry'
urlpatterns = [
    path('price', views.price, name='price'),
    path('kids', views.kids, name='kids'),
    path('doctors', views.doctors, name='doctors'),
    path('license', views.license, name='license'),
    path('gallery', views.gallery, name='gallery'),
    path('about_us', views.about_us, name='about_us'),
    path('', views.index, name='index'),
]