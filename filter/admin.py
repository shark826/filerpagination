from django.contrib import admin
from .models import *
# Register your models here.
class PdAdmin(admin.ModelAdmin):
    list_display = ('nom','fam','name','fname','dr')


admin.site.register(Pd, PdAdmin)