import os

from django.db import models


class TicketBus(models.Model):
    bus = models.CharField(max_length=100)
    image = models.ImageField(upload_to=os.path.join('tourisme', 'photo'), null=True, blank=True)
    depart = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=100)

class Hebergement(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def calculate_total_price(self, duration):

        total_price = self.price_per_night * duration
        return total_price


class TicketBusetHebergement(models.Model):
    ticket_bus = models.ForeignKey(TicketBus, on_delete=models.CASCADE)
    Hebergement = models.ForeignKey(Hebergement, on_delete=models.CASCADE)

class Sitetour(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    region = models.CharField(max_length=100)

class Guide(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=100)

class SitetourEtGuide(models.Model):
    Sitetour = models.ForeignKey('Sitetour', on_delete=models.CASCADE)
    guide = models.ForeignKey('Guide', on_delete=models.CASCADE)

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    region = models.CharField(max_length=100)