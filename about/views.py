from django.shortcuts import render
from .models import Gallery

# Create your views here.
def about(request):
    gal={
       "gal" : Gallery.objects.all()
    }

    return render(request, 'about.html', gal)