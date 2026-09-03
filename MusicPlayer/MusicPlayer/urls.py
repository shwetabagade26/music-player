from django.contrib import admin
from django.urls import path, include, re_path  # Added re_path here
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve           # Added serve here

urlpatterns = [
    path('admin/', admin.site.urls),
    # This tells Django to send all other traffic to your 'App' folder
    path('', include('App.urls')),
]

# This serves your uploaded audio/images during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# NEW: This forces Django to serve media files in production on Render
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]