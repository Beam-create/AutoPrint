from django.http import request
from django.shortcuts import render

#Ajouter cette import au début, retirer quand on utilise un template
#from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'interface/home.html')

def interaction(request):
    return render(request, 'interface/interaction.html')

def buttons(request):
    return render(request, 'interface/buttons.html')

def Printer_status(request):
    return render(request, 'interface/Printer_status.html')