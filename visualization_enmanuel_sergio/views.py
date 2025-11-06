from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Count
from management_enmanuel_sergio.models import Reserva
import csv
from django.http import HttpResponse

class ReservaStatisticsView(TemplateView):
    template_name = 'visualization/reserva_statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reservas_por_laboratorio'] = Reserva.objects.values('laboratorio').annotate(count=Count('id'))
        context['reservas_por_estado'] = Reserva.objects.values('estado').annotate(count=Count('id'))
        return context

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reservas.csv"'

    writer = csv.writer(response)
    writer.writerow(['Usuario', 'Laboratorio', 'Fecha', 'Hora Inicio', 'Hora Fin', 'Estado'])

    reservas = Reserva.objects.all().values_list('usuario__username', 'laboratorio', 'fecha', 'hora_inicio', 'hora_fin', 'estado')
    for reserva in reservas:
        writer.writerow(reserva)

    return response
