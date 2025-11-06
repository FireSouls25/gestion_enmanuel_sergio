from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLES = [
        ('docente', 'Docente'),
        ('administrador', 'Administrador'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLES, default='docente')

    def __str__(self):
        return f'{self.user.username} - {self.get_role_display()}'
