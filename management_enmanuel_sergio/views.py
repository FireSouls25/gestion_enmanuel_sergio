from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Reserva
from autentication_enmanuel_sergio.models import Profile

class DocenteRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.profile.role == 'docente'

class AdministradorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.profile.role == 'administrador'

class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'management/reserva_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        
        fecha = self.request.GET.get('fecha')
        laboratorio = self.request.GET.get('laboratorio')

        if fecha:
            queryset = queryset.filter(fecha=fecha)
        if laboratorio:
            queryset = queryset.filter(laboratorio__icontains=laboratorio)

        return queryset

class ReservaCreateView(LoginRequiredMixin, DocenteRequiredMixin, CreateView):
    model = Reserva
    template_name = 'management/reserva_form.html'
    fields = ['laboratorio', 'fecha', 'hora_inicio', 'hora_fin', 'motivo']
    success_url = reverse_lazy('management:reserva_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ReservaUpdateView(LoginRequiredMixin, DocenteRequiredMixin, UpdateView):
    model = Reserva
    template_name = 'management/reserva_form.html'
    fields = ['laboratorio', 'fecha', 'hora_inicio', 'hora_fin', 'motivo']
    success_url = reverse_lazy('management:reserva_list')

    def test_func(self):
        reserva = self.get_object()
        return super().test_func() and self.request.user == reserva.usuario and reserva.estado == 'pendiente'

class ReservaDeleteView(LoginRequiredMixin, DocenteRequiredMixin, DeleteView):
    model = Reserva
    template_name = 'management/reserva_confirm_delete.html'
    success_url = reverse_lazy('management:reserva_list')

    def test_func(self):
        reserva = self.get_object()
        return super().test_func() and self.request.user == reserva.usuario and reserva.estado == 'pendiente'

class AdminReservaListView(LoginRequiredMixin, AdministradorRequiredMixin, ListView):
    model = Reserva
    template_name = 'management/admin_reserva_list.html' # New template for admin list
    context_object_name = 'reservas'

    def get_queryset(self):
        queryset = Reserva.objects.all()
        
        fecha = self.request.GET.get('fecha')
        laboratorio = self.request.GET.get('laboratorio')
        usuario = self.request.GET.get('usuario')
        estado = self.request.GET.get('estado')

        if fecha:
            queryset = queryset.filter(fecha=fecha)
        if laboratorio:
            queryset = queryset.filter(laboratorio__icontains=laboratorio)
        if usuario:
            queryset = queryset.filter(usuario__username__icontains=usuario)
        if estado:
            queryset = queryset.filter(estado=estado)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reserva_estados'] = Reserva.ESTADO_CHOICES
        return context

class AdminReservaUpdateView(LoginRequiredMixin, AdministradorRequiredMixin, UpdateView):
    model = Reserva
    template_name = 'management/admin_reserva_form.html' # New template for admin update
    fields = ['laboratorio', 'fecha', 'hora_inicio', 'hora_fin', 'estado', 'motivo']
    success_url = reverse_lazy('management:admin_reserva_list')
