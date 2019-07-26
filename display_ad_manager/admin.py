from django.contrib import admin
from .models import Placement, Banner
from django.template.loader import render_to_string
from django import forms
from django.urls import reverse

url = reverse('placements', args = [1])

rendered = render_to_string('placement_template.html',{'placement_url': url})

class PlacementForm(forms.ModelForm):
    tag = forms.CharField(initial = rendered)

    class Meta:
        model = Placement
        fields = '__all__'

class PlacementAdmin(admin.ModelAdmin):
    form = PlacementForm

admin.site.register(Placement, PlacementAdmin)
admin.site.register(Banner)
