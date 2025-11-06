from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Reserva

class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'management/reserva_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Reserva.objects.all()
        return Reserva.objects.filter(usuario=self.request.user)

class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    template_name = 'management/reserva_form.html'
    fields = ['laboratorio', 'fecha', 'hora_inicio', 'hora_fin', 'motivo']
    success_url = reverse_lazy('management:reserva_list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class ReservaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Reserva
    template_name = 'management/reserva_form.html'
    fields = ['laboratorio', 'fecha', 'hora_inicio', 'hora_fin', 'motivo']
    success_url = reverse_lazy('management:reserva_list')

    def test_func(self):
        reserva = self.get_object()
        return self.request.user == reserva.usuario and reserva.estado == 'pendiente'

class ReservaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reserva
    template_name = 'management/reserva_confirm_delete.html'
    success_url = reverse_lazy('management:reserva_list')

    def test_func(self):
        reserva = self.get_object()
        return self.request.user == reserva.usuario and reserva.estado == 'pendiente'
