from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse

class Placement(models.Model):
    name = models.CharField(max_length=100)

    def get_tag(self):
        url = 'http://127.0.0.1:8000' + reverse('placement', args = [self.pk])
        rendered = render_to_string('placement_template.html',{'placement_url': url})
        return rendered

    def __str__(self):
        return self.name

class Banner(models.Model):
    campaign_name = models.CharField(max_length=100)
    banner_code = models.TextField()
    display_count = models.IntegerField(default=0)
    active_banner = models.BooleanField(default=True)
    placements = models.ManyToManyField(Placement)



    def __str__(self):
        return self.campaign_name
