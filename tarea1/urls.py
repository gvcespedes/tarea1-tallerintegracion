"""tarea1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import home, lista_datos_usuario, datos_ciudades, barra_busqueda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('consulta1/<id>', lista_datos_usuario),
    path('consulta2/<id>', datos_ciudades),
    path('buscar/', barra_busqueda)
]
