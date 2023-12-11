from django.shortcuts import render
from .models import ContactCard

def wildcard_home(request):
    cards = ContactCard.objects.all()
    return render(request, 'wildcard/home.html', {'cards': cards})
