from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autentication_enmanuel_sergio.urls')),
    path('management/', include('management_enmanuel_sergio.urls')),
    path('visualization/', include('visualization_enmanuel_sergio.urls', namespace='visualization')),
]
