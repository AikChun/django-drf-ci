from django.shortcuts import render
from .serializers import EventSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from .models import Event


# Create your views here.
class EventListCreate(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
