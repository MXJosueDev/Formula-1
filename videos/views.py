from django.shortcuts import render
from .models import Video

from random import choice, choices

# Create your views here.
def index(request):
    videos = Video.objects.all()

    most_seen = choice(videos.filter(category='Most Seen'))
    news = choices(videos.filter(category='News'), k=3)

    return render(request, 'videos/videos.html', {'most_seen': most_seen, 'news': news})