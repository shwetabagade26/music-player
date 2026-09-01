from django.shortcuts import render, get_object_or_404
from .models import Song, Playlist

def index(request):
    # Fetch all songs for the main page
    songs = Song.objects.all()
    context = {
        'songs': songs,
        'playlists': Playlist.objects.all(),
        'active_playlist': None,
    }
    return render(request, 'index.html', context)


def playlist_detail(request, pk):
    # Fetch songs only for a specific playlist
    playlist = get_object_or_404(Playlist, pk=pk)
    songs = playlist.songs.all()
    context = {
        'songs': songs,
        'playlists': Playlist.objects.all(),
        'active_playlist': playlist,
    }
    return render(request, 'index.html', context)   