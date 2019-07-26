from django.contrib import admin
from .models import Placement, Banner
from django.template.loader import render_to_string
from django import forms

rendered = render_to_string('placement_template.html',{'placement_url': '10'})

class PlacementForm(forms.ModelForm):
    tag = forms.CharField(initial = rendered)

    class Meta:
        model = Placement
        fields = '__all__'

class PlacementAdmin(admin.ModelAdmin):
    form = PlacementForm

admin.site.register(Placement, PlacementAdmin)
admin.site.register(Banner)
