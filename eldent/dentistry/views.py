from django.http import Http404
from django.shortcuts import render
from .models import Doctor, Services, Galery_photo

def index(request):
    print('index')
    doctor_list = Doctor.objects.all()
    price_list = Services.objects.all()
    photo_list = Galery_photo.objects.all()
    context = {
        'doctor_list': doctor_list,
        'price_list': price_list,
        'photo_list': photo_list,
    }
    return render(request, 'dentistry/index.html', context)

def price(request):
    print('price')
    price_list = Services.objects.all()
    context = {
        'price_list': price_list,
    }
    return render(request, 'dentistry/price.html', context)

def doctors(request):
    print('doctors')
    doctor_list = Doctor.objects.all()
    context = {
        'doctor_list': doctor_list,
    }
    return render(request, 'dentistry/doctors.html', context)
def gallery(request):
    print('gallery')
    photo_list = Galery_photo.objects.all()
    context = {
        'photo_list': photo_list,
    }
    return render(request, 'dentistry/gallery.html', context)
def about_us(request):
    print('about_us')
    doctor_list = Doctor.objects.all()
    context = {
        'doctor_list': doctor_list,
    }
    return render(request, 'dentistry/about_us.html', context)