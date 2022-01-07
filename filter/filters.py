import django_filters
from django.forms import DateInput, TextInput, IntegerField
from django_filters.widgets import RangeWidget

from .models import Pd

class PdFilter (django_filters.FilterSet):

    nom = django_filters.CharFilter(field_name='nom', lookup_expr='icontains', label='',
                                      widget=TextInput(attrs={'placeholder': 'Номер дела',
                                                              'type':'number', 'min':'1',
                                                              'data-mask':"00000000",
                                                              "style":"margin:0.5rem 0 0 0",}))
    fam = django_filters.CharFilter(field_name='fam', lookup_expr='istartswith', label='',
                                     widget=TextInput(attrs={'placeholder': 'Фамилия',
                                                             "style":"margin:0.5rem 0 0 0",}))
    name = django_filters.CharFilter(field_name='name', lookup_expr='istartswith', label='',
                                     widget=TextInput(attrs={'placeholder': 'Имя',
                                                             "style":"margin:0.5rem 0 0 0",}))
    fname = django_filters.CharFilter(field_name='fname', lookup_expr='istartswith', label='',
                                     widget=TextInput(attrs={'placeholder': 'Отчество',
                                                             "style":"margin:0.5rem 0 0 0",}))
    dr = django_filters.DateFilter(field_name='dr', lookup_expr=('lte'),
                                         label='Дата рождения:  ПО',
                                         widget=TextInput(attrs={'placeholder': 'ДД.ММ.ГГГГ', 'type':'date',
                                                                 'required': 'true'}))
    class Meta:
        model = Pd
        fields = [ 'nom', 'fam', 'name', 'fname', 'dr' ]

class BookFilterSet(django_filters.FilterSet):
    def __init__(self, data, *args, **kwargs):
        data = data.copy()
        data.setdefault('format', 'paperback')
        data.setdefault('order', '-added')
        super().__init__(data, *args, **kwargs)