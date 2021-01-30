from django.shortcuts import render, redirect
from .models import Pokemon
# Create your views here.
# Add the following import


# Define the home view
def home(request):
  return render(request, 'home.html')
def about(request):
   return render(request, 'about.html')
   
def pokemon_index(request):
    return render(request, 'pokemon/index.html', {'pokemon': pokemon_index})