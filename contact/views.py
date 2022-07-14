from django.shortcuts import render
from .models import Giveaway

# Create your views here.
def contact(request):
    giveaway = {
        "giveaway" : Giveaway.objects.all()
    }
    return render(request, 'contact.html', giveaway)