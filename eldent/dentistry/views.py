from django.http import Http404
from django.shortcuts import render
from .models import Doctor

def index(request):
    doctor_list = Doctor.objects.all()
    context = {
        'doctor_list': doctor_list,
    }
    return render(request, 'dentistry/index.html', context)