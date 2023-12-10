from django.shortcuts import render
from .models import contactcard


def wildcard_home(request):
    cards = contactcard.objects.all()
    return render(request, 'wildcard/home.html', {'cards': cards})