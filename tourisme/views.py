from django.shortcuts import render, redirect
from .models import *
from .forms import *

def liste_site_tour(request):
    return render(request, 'liste_site_tour.html')

def create_site_tour(request):
    if request.method == 'POST':
        form = SiteTouristiqueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_site_tour')
    else:
        form = SiteTouristiqueForm()
    return render(request, 'create_site_tour.html', {'form': form})






def hebergement(request):

    hebergements = Hebergement.objects.all()

    return render(request, 'hebergement.html', {'hebergements': hebergements})

def create_henergement(request):
    if request.method == 'POST':
        form = HebergementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hebergement')
    else:
        form = HebergementForm()
    return render(request, 'create_hebergement.html', {'form': form})



def location(request):

    return render(request, 'location.html')
def create_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('location')
    else:
        form = LocationForm()
    return render(request, 'create_location.html', {'form': form})



def ticket(request):
    tickets = TicketBus.objects.all()

    return render(request, 'ticket.html' ,{'tickets': tickets})
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket')
    else:
        form = TicketForm()
    return render(request, 'create_ticket.html', {'form': form})


def Guide(request):

    return render(request, 'guide.html')
def create_guide(request):
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Guide')
    else:
        form = GuideForm()
    return render(request, 'create_guide.html', {'form': form})



def ticketHotel(request):

    return render(request, 'ticketHotel.html')
