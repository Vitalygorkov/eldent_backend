from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import mptt
from datetime import date

class Category(MPTTModel):
    name = models.CharField("Категория",max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, verbose_name='URL на английском, например "Category"', unique=True)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    def get_absolute_url(self):
        return f'/{self.url}/'
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name
    class MPTTMeta:
        order_insertion_by = ['-tree_id']
    class Meta:
        db_table = "category"
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('tree_id','level')
mptt.register(Category, order_insertion_by=['name'])

class Doctor(models.Model):
    surname = models.CharField("фамилия", max_length=90)
    name = models.CharField("Имя", max_length=90)
    middle_name = models.CharField("Отчество", max_length=90, blank=True)
    image = models.ImageField("Фото", upload_to="photo/", null=True, blank=True)
    experience = models.DateField('Дата начала стажа',)
    # def get_experience_age(self):
    #     print(elf.experience-date.today()
    #     return self.experience-date.today()
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Services(models.Model):
    name = models.CharField("Услуга", max_length=500)
    description = models.TextField('Описание', blank=True)  # описание
    price = models.IntegerField("Стоимость", blank=True)


class Reviews(models.Model):
    """Отзывы"""

