from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import ContactInfo
import requests
from django.http import JsonResponse

# Vista para la página principal (profile)
def profile_view(request):
    return render(request, "profile.html")

# Vista para la página de servicios
def services_view(request):
    # Verificar si hay un parámetro 'tipo' en la solicitud GET
    tipo = request.GET.get('tipo')
    
    if tipo:
        # Lógica para manejar diferentes tipos de solicitudes
        if tipo == 'api':
            response = requests.get("https://api.chucknorris.io/jokes/random")
            if response.status_code == 200:
                joke_data = response.json()
                return JsonResponse(joke_data)
            else:
                return JsonResponse({"error": "No se pudo obtener el chiste"}, status=500)
        # Agregar más condiciones para otros tipos de solicitudes si es necesario
        # elif tipo == 'otro-tipo':
        #     # Lógica para otro tipo
        #     pass
    
    return render(request, "service.html")
# Vista para la página de descripción de servicios
def description_view(request):
    return render(request, "description.html")

# Vista para el formulario de contacto
def contact_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("message")

        if not full_name or not email:
            messages.error(request, "El nombre completo y el correo electrónico son obligatorios.")
        else:
            # Guarda en la base de datos
            ContactInfo.objects.create(
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                message=message
            )

            # Enviar un correo
            send_mail(
                subject=f"Nuevo mensaje de {full_name}",
                message=f"Nombre: {full_name}\nCorreo: {email}\nTeléfono: {phone_number}\n\nMensaje:\n{message}",
                from_email="tu_correo@example.com",  # Configura este correo
                recipient_list=["tu_correo@example.com"],  # Tu correo de destino
                fail_silently=False,
            )

            messages.success(request, "¡Tu mensaje ha sido enviado con éxito!")
            return redirect("contactapp:contact_form")
    return render(request, "contact_form.html")

