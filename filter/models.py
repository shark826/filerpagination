from django.db import models

# Create your models here.
class Pd(models.Model):

    nom = models.IntegerField(unique = True, verbose_name="Номер дела")
    fam = models.CharField(max_length=25, verbose_name="Фамилия")
    name = models.CharField(max_length=25, verbose_name="Имя")
    fname = models.CharField(max_length=25, null =True, blank=True, verbose_name="Отчество")
    dr = models.DateField(verbose_name="Дата рождения")

