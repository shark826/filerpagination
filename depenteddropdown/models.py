from django.db import models

# Create your models here.
class Persons(models.Model):

    nom = models.IntegerField(unique = True, verbose_name="Номер дела")
    fam = models.CharField(max_length=25, verbose_name="Фамилия")
    name = models.CharField(max_length=25, verbose_name="Имя")
    dr = models.DateField(verbose_name="Дата рождения")
    gor = models.ForeignKey('Gorod', null=True, on_delete=models.PROTECT, verbose_name="Населенный пункт")
    ul = models.ForeignKey('Ulica', null=True, on_delete=models.PROTECT, verbose_name="Улица")

class Gorod(models.Model):
    name = models.CharField(max_length=35, verbose_name="Название")


class Ulica(models.Model):
    idgorod = models.ForeignKey('Gorod', null=True, on_delete=models.PROTECT, verbose_name="Город")
    name = models.CharField(max_length=35, verbose_name="Название")