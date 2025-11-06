from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import HomeView, RegisterView

app_name = 'autentication_enmanuel_sergio'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='autentication/login.html', next_page=reverse_lazy('management:reserva_list')), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('autentication_enmanuel_sergio:login')), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
