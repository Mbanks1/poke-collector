from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')
  def about(request):
      return HttpResponse('<h1>About Pokemon<h1>')