from django.urls import path
from .views import (
    ReservaListView,
    ReservaCreateView,
    ReservaUpdateView,
    ReservaDeleteView,
    AdminReservaListView,
    AdminReservaUpdateView,
)

app_name = 'management_enmanuel_sergio'

urlpatterns = [
    path('', ReservaListView.as_view(), name='reserva_list'),
    path('crear/', ReservaCreateView.as_view(), name='reserva_create'),
    path('<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva_update'),
    path('<int:pk>/eliminar/', ReservaDeleteView.as_view(), name='reserva_delete'),
    path('admin/reservas/', AdminReservaListView.as_view(), name='admin_reserva_list'),
    path('admin/reservas/<int:pk>/editar/', AdminReservaUpdateView.as_view(), name='admin_reserva_update'),
]
