from django.db import models


class Placement(models.Model):
    name = models.CharField(max_length=100)

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
