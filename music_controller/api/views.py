from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
# Create your views here. 

# This view gives a view to create object to the

class RoomView(generics.CreateAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer

# This gives list of created object
'''
class RoomView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
'''