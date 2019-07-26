from django.contrib import admin
from .models import Placement, Banner
from django import forms


class PlacementForm(forms.ModelForm):

    tag = forms.CharField(initial = '')
    def __init__(self, *args, **kwargs):
        super(PlacementForm, self).__init__(*args, **kwargs)
        print(self.instance)
        self.initial['tag'] = self.instance.get_tag()



    class Meta:
        model = Placement
        fields = '__all__'

class PlacementAdmin(admin.ModelAdmin):
    form = PlacementForm

admin.site.register(Placement, PlacementAdmin)
admin.site.register(Banner)
