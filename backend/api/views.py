from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import User
from rest_framework.generics import CreateAPIView


# Create your views here.

@api_view(['POST'])

def Register(request):
    query = User.objects.all()
