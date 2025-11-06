from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View

class HomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('management:reserva_list'))
        return redirect(reverse_lazy('autentication_enmanuel_sergio:login'))

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'autentication/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('autentication_enmanuel_sergio:login'))
        return render(request, 'autentication/register.html', {'form': form})
