from django.urls import path
from . import views

app_name = "contactapp"
urlpatterns = [
    path("", views.profile_view, name="profile"),  # Página principal
    path("contact_form/", views.contact_view, name="contact_form"),  # Página del formulario 
    path("services/", views.services_view, name="services"),  # Página de Servicios
    path("description/", views.description_view, name="description")  # Página de Servicios
]
