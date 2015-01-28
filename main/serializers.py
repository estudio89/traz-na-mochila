"""
Serializers
"""

from rest_framework import serializers
from main.models import *

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City

class UserProfileSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = UserProfile
        exclude = ('id',)

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(source='userprofile')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'profile')

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country

class TripSerializer(serializers.ModelSerializer):
    traveler = UserSerializer()
    trip_to = CountrySerializer()

    class Meta:
        model = Trip