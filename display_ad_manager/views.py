from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def placement(request, placement_id):
    return HttpResponse(placement_id)
