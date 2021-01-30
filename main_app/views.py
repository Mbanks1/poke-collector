from django.shortcuts import render, redirect

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, '<h1>Hello</h1>')
def about(request):
   return render(request, 'about.html')