"""
Model classes
"""

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	phone_number = models.CharField(max_length=15)
	city = models.ForeignKey('main.City')
	zip_code = models.CharField(max_length=20)
	latitude = models.FloatField()
	longitude = models.FloatField()

class Trip(models.Model):
	traveler = models.ForeignKey(User)
	trip_to = models.ForeignKey('main.Country')
	departure_date = models.DateField()
	return_date = models.DateField()
	info = models.TextField()

class City(models.Model):
	name = models.CharField(max_length=100)
	latitude = models.FloatField()
	longitude = models.FloatField()

class Country(models.Model):
	name = models.CharField(max_length=100)