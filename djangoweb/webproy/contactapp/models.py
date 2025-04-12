from django.db import models

class ContactInfo(models.Model):
    full_name = models.CharField(max_length=200)  # Nombre completo
    email = models.EmailField()  # Correo electrónico
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Número de teléfono
    message = models.TextField(blank=True, null=True)  # Mensaje opcional
    submitted_at = models.DateTimeField(auto_now_add=True)  # Fecha y hora en que se registró la información

    def __str__(self):
        return f"{self.full_name} - {self.email}"
