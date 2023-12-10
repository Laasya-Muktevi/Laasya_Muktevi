from django.db import models

# Create your models here.

class contactcard(models.Model):
    card_name = models.CharField(max_length=100, unique=True)
    card_email = models.EmailField(unique=True)
    card_phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.card_name