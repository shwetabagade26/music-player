from django.urls import path
from . import views

app_name = "App"

urlpatterns = [
    path("", views.index, name="index"),
    path("playlist/<int:pk>/", views.playlist_detail, name="playlist_detail"),
]