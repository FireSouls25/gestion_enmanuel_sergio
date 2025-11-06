from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm
from .models import Profile

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if hasattr(request.user, 'profile') and request.user.profile.role == 'administrador':
                return redirect(reverse_lazy('management:admin_reserva_list'))
            return redirect(reverse_lazy('management:reserva_list'))
        return redirect(reverse_lazy('autentication_enmanuel_sergio:login'))

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'autentication/register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('autentication_enmanuel_sergio:login'))
        return render(request, 'autentication/register.html', {'form': form})
