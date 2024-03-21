from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def destination(request):
    return render(request, 'destination.html')

def ticket(request):
    return render(request, 'ticket.html')

def contact(request):
    return render(request, 'contact.html')