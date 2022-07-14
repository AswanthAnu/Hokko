from django.shortcuts import render
from .models import Destination
from django.views.decorators.cache import cache_control



def home(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests' : dests})
