from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='autentication_enmanuel_sergio:home'), name='home'),
    path('admin/', admin.site.urls),
    path('auth/', include('autentication_enmanuel_sergio.urls')),
    path('management/', include('management_enmanuel_sergio.urls')),
    path('visualization/', include('visualization_enmanuel_sergio.urls', namespace='visualization')),
]
