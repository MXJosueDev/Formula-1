from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pilot
from equipos.models import Team
from .forms import PilotForm

# Create your views here.
def index(request):
    pilots = Pilot.objects.all().order_by('-points')

    return render(request, 'pilotos/pilotos.html', {'pilots': pilots})

@login_required
def create_pilot(request):
    if request.method == 'POST':
        form = PilotForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('pilotos')

    teams = Team.objects.all().order_by('name')
    return render(request, 'pilotos/create_pilot.html', {'teams': teams})

@login_required
def edit_pilot(request, pilot_id):
    pilot = get_object_or_404(Pilot, pk=pilot_id)

    if request.method == 'POST':
        form = PilotForm(request.POST, request.FILES, instance=pilot)

        if form.is_valid():
            form.save()

            return redirect('pilotos')

    teams = Team.objects.all().order_by('name')
    return render(request, 'pilotos/edit_pilot.html', {'pilot': pilot, 'teams': teams})

@login_required
def delete_pilot(request, pilot_id):
    pilot = get_object_or_404(Pilot, pk=pilot_id)
    pilot.delete()

    return redirect('pilotos')