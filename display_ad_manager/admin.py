from django.contrib import admin
from .models import Placement, Banner

from django import forms

admin.site.register(Placement)
admin.site.register(Banner)


class PlacementForm(forms.ModelForm):
    list_display = ('name')

    class Meta:
        model = Placement
        exclude = ['name']

class PlacementAdmin(admin.ModelAdmin):
    list_display = ('name')
    exclude = ['name']
    form = PlacementForm
