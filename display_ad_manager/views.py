from django.shortcuts import render
from .utils import converter
# Create your views here.
from django.http import HttpResponse
from display_ad_manager.models import Banner, Placement

def placement(request, placement_id):
    placement = Placement.objects.get(pk=placement_id)
    display_banner = placement.banner_set.filter(active_banner=True).order_by('?').all()[0]
    impressions = display_banner.display_count
    display_banner.display_count = impressions + 1
    display_banner.save()
    return HttpResponse(converter(display_banner.banner_code), content_type = "text/javascript")
