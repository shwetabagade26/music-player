from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    image = models.ImageField(upload_to='covers/')
    audio_file = models.FileField(upload_to='audio/', blank=True, null=True)
    audio_link = models.CharField(max_length=200, blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} — {self.artist}"


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='playlist_covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    songs = models.ManyToManyField(Song, related_name='playlists', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name