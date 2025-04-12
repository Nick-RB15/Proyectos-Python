from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("contactapp.urls")),  # Apunta a las rutas definidas en contactapp
    path("admin/", admin.site.urls),       # Ruta para el panel de administración
]
