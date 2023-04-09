from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Doctor, Galery_photo, Services


admin.site.register(Doctor)
admin.site.register(Galery_photo)
admin.site.register(Services)


admin.site.site_title = "Стоматология Елизавета"
admin.site.site_header = "Стоматология Елизавета"