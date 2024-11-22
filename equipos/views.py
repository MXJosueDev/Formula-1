from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Team
from .forms import TeamForm
from pilotos.models import Pilot

# Create your views here.
def index(request):
    teams = Team.objects.all()

    for team in teams:
        pilots = Pilot.objects.filter(team=team)
        team.points = sum(pilot.points for pilot in pilots)
        team.save()

    teams = teams.order_by('-points')

    return render(request, 'equipos/equipos.html', {'teams': teams})

@login_required
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('equipos')

    return render(request, 'equipos/create_team.html')

@login_required
def edit_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)

        if form.is_valid():
            form.save()

            return redirect('equipos')

    return render(request, 'equipos/edit_team.html', {'team': team})

@login_required
def delete_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    team.delete()

    return redirect('equipos')