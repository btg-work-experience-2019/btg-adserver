from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the BTG adserver website.")
def main(request):
    return HttpResponse("")
def placements(request):
    return HttpResponse("")
