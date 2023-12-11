from django.shortcuts import render, redirect
from .models import ContactCard
from django.forms import ModelForm
from django.core.exceptions import ValidationError

def wildcard_home(request):
    cards = ContactCard.objects.all()
    return render(request, 'wildcard/home.html', {'cards': cards})

class ContactCardForm(ModelForm):
    class Meta:
        model = ContactCard
        fields = ['card_name', 'card_email', 'card_phone']


def create_contact_card(request):
    if request.method == 'POST':
        form = ContactCardForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('wildcard_home')
        except ValidationError as e:
            if 'card_name' in e.message_dict:
                form.add_error('card_name', 'Name already exists.')
            if 'card_email' in e.message_dict:
                form.add_error('card_email', 'Email already exists.')
    else:
        form = ContactCardForm()

    return render(request, 'wildcard/create_contact_card.html', {'form': form})
