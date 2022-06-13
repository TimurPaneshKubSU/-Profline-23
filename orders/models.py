
from django.db import models
from django.forms import CharField
from salons.models import Salon

class Service(models.Model):
    """
    name -models.CharField
    url - models.CharField

    """

    FIO = models.CharField(verbose_name='Нименование услуги', max_length=256)
    duration = models.CharField(verbose_name='Время оказания', max_length=256)
    price = models.CharField(verbose_name='Цена', max_length=256)
    salon-names = models.ForeignKey(Salon, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
