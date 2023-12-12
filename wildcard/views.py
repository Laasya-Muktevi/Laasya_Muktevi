from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactCard
from django.forms import ModelForm
from django.core.exceptions import ValidationError

def wildcard_home(request):
    cards = ContactCard.objects.all()
    return render(request, 'wildcard/home.html', {'cards': cards})

class ContactCardForm(ModelForm):
    class Meta:
        model = ContactCard
        fields = ['card_name', 'card_email', 'card_phone', 'message']

def create_contact_card(request):
    if request.method == 'POST':
        form = ContactCardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wildcard_home')
        else:
            # Form validation errors are automatically handled by Django
            pass
    else:
        form = ContactCardForm()

    return render(request, 'wildcard/create_contact_card.html', {'form': form})

def card_info(request, card_id):
    card = get_object_or_404(ContactCard, pk=card_id)
    return render(request, 'wildcard/card_info.html', {'card': card})

def update_contact_card(request, card_id):
    card = get_object_or_404(ContactCard, pk=card_id)
    if request.method == 'POST':
        form = ContactCardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('wildcard_home')
    else:
        form = ContactCardForm(instance=card)

    return render(request, 'wildcard/update_contact_card.html', {'form': form, 'card_id': card_id})