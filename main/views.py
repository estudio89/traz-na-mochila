"""
Views
"""

from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.contrib import auth
from rest_framework.renderers import JSONRenderer
from main.models import *
from main.serializers import *

def index(request):
    return render_to_response('base.html', {'test':'index'}, context_instance=RequestContext(request))

def trip(request, trip_id=None):
    if request.method == 'GET':
        if trip_id:
            # Return a particular trip
            serializer = TripSerializer(get_object_or_404(Trip, pk=trip_id))
        else:
            # Return a list of all trips
            serializer = TripSerializer(Trip.objects.all(), many=True)
    elif request.method == 'POST':
        # Create a new trip
        traveler = request.user
        trip_to = request.POST.get('trip_to')
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')
        info = request.POST.get('info')
        trip = Trip(traveler=traveler, trip_to=trip_to, departure_date=departure_date, return_date=return_date, info=info)
        trip.save()
        serializer = TripSerializer(trip)
    elif request.method == 'DELETE':
        # Delete a particular trip
        trip = get_object_or_404(Trip, pk=trip_id)
        # Check if request.user is the trip's traveler
        if trip.traveler == request.user:
            trip.delete()
            json = "{'return':'OK'}"
        else:
            json = "{'return':'ERROR'}"
    else:
        json = 'NONE'

    json = JSONRenderer().render(serializer.data)

    return render_to_response('base.html', {'test':json}, context_instance=RequestContext(request))

def message(request, receiver_id):
    return render_to_response('base.html', {'test':'new message'}, context_instance=RequestContext(request))

def contact(request):
    return render_to_response('base.html', {'test':'contact'}, context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")