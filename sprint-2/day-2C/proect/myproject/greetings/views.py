from django.shortcuts import render
from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("Welcome to our Django App!")

def greet_view(request, username):
    return HttpResponse(f"Hello, {username}!")

def farewell_view(request, username):
    return HttpResponse(f"Goodbye, {username}!")
