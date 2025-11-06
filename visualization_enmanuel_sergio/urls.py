from django.urls import path
from .views import ReservaStatisticsView, export_csv

app_name = 'visualization_enmanuel_sergio'

urlpatterns = [
    path('statistics/', ReservaStatisticsView.as_view(), name='reserva_statistics'),
    path('export/csv/', export_csv, name='export_csv'),
]
