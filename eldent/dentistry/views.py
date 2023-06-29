from django.http import Http404
from django.shortcuts import render, redirect
from .models import Doctor, Services, Galery_photo
from django.core.mail import BadHeaderError, send_mail
from .forms import ContactForm

# def email(subject, content):
#     send_mail(subject, content, 'auto-message@elizaveta-dent55.ru', ['clients@elizaveta-dent55.ru'])

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
    
def contact_view(request):
    print('контакт вью')
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        print('elif post')
        form = ContactForm(request.POST)
        # print(form)
        if form.is_valid():
            print('иф форм валид')
            name = form.cleaned_data['name']
            print(name)
            if name == 'name':
                print('name пусто можно отправлять')
            fio = form.cleaned_data['fio']
            print(fio)
            email_address = form.cleaned_data['email_address']
            print(email_address)
            phone = form.cleaned_data['phone']
            print(phone)
            subject = "Заявка от: " + fio
            content = 'ФИО: ' + fio + " Телефон: " + phone + ' Е-мейл: ' + email_address
            try:
                print('отправка письма')
                send_mail(subject, content, 'auto-message@elizaveta-dent55.ru', ['clients@elizaveta-dent55.ru'], fail_silently=False,)
                # send_mail(f'{subject} от {from_email}', message,
                #           DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                print('ексепшн')
                return HttpResponse('Ошибка в теме письма.')
            return redirect('/success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "dentistry/contact_form.html", {'form': form})

def success_view(request):
    # return HttpResponse('Приняли! Спасибо за вашу заявку.')
    return render(request, 'dentistry/success.html')


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

def kids(request):
    print('kids')
    price_list = Services.objects.all()
    context = {
        'price_list': price_list,
    }
    return render(request, 'dentistry/kids.html', context)

def doctors(request):
    print('doctors')
    doctor_list = Doctor.objects.all()
    context = {
        'doctor_list': doctor_list,
    }
    return render(request, 'dentistry/doctors.html', context)

def license(request):
    print('license')
    doctor_list = Doctor.objects.all()
    context = {
        'doctor_list': doctor_list,
    }
    return render(request, 'dentistry/license.html', context)

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