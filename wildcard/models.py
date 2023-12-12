from django.db import models
from django.core.validators import RegexValidator

class ContactCard(models.Model):
    card_name = models.CharField(max_length=100, unique=True)
    card_email = models.EmailField(unique=True)
    card_phone = models.CharField(
        max_length=10, 
        blank=True,
        validators=[RegexValidator(r'^\d{1,10}$', 'Only numeric characters are allowed.')])
    message = models.TextField(blank=True)

    def __str__(self):
        return self.card_name
