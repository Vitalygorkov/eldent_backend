from django import forms
from captcha.fields import ReCaptchaField
# from captcha.widgets import ReCaptchaV3
# from captcha.widgets import ReCaptchaV2Checkbox
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

class ContactForm(forms.Form):
    fio = forms.CharField(max_length=120, required=True)
    email_address = forms.EmailField(max_length=150, required=False)
    phone = forms.CharField(max_length=30, required=True)
    name = forms.CharField(max_length=30, required=True)
    captcha = ReCaptchaField()
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    # captcha = ReCaptchaField(widget=ReCaptchaV3)
