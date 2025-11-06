from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'laboratorio', 'fecha', 'hora_inicio', 'hora_fin', 'estado')
    list_filter = ('estado', 'fecha', 'laboratorio')
    search_fields = ('usuario__username', 'laboratorio')
    actions = ['aprobar_reservas', 'rechazar_reservas']

    def aprobar_reservas(self, request, queryset):
        queryset.update(estado='aprobada')
    aprobar_reservas.short_description = "Aprobar reservas seleccionadas"

    def rechazar_reservas(self, request, queryset):
        queryset.update(estado='rechazada')
    rechazar_reservas.short_description = "Rechazar reservas seleccionadas"
