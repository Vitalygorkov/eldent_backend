from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Doctor, Category

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Doctor)


admin.site.site_title = "Стоматология Елизавета"
admin.site.site_header = "Стоматология Елизавета"