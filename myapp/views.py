from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
import requests

# Create your views here.

def home(request):
    i = 1
    while True:
        response = requests.get(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/53372/users?_page={i}').json()
        if i == 1:
            resp = response
        if len(response)==0:
            break
        if i != 1:
            resp.extend(response)
        i += 1

    i=1
    while True:
        response2 = requests.get(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/53372/cities?_page={i}').json()
        if i == 1:
            resp2 = response2
        if len(response2)==0:
            break
        if i != 1:
            resp2.extend(response2)
        i += 1
    return render(request, 'inicio.html', {'usuarios': resp, 'ciudades': resp2})


def lista_datos_usuario(request, id):
    i = 1
    while True:
        response = requests.get(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/53372/users/{id}/credit-cards?_page={i}').json()
        if i == 1:
            resp = response
        if len(response)==0:
            break
        if i != 1:
            resp.extend(response)
        i += 1

    i=1
    while True:
        response2 = requests.get(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/53372/users/{id}/addresses?_page={i}').json()
        if i == 1:
            resp2 = response2
        if len(response2)==0:
            break
        if i != 1:
            resp2.extend(response2)
        i += 1
    return render(request, 'info_usuarios.html', {'tarjetas': resp, 'direcciones': resp2})

def datos_ciudades(request, id):
    i = 1
    while True:
        response = requests.get(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/53372/cities?_page={i}').json()
        if i == 1:
            resp = response
        if len(response)==0:
            break
        if i != 1:
            resp.extend(response)
        i += 1

    i=1
    while True:
        response2 = requests.get(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/53372/users?_page={i}').json()
        if i == 1:
            resp2 = response2
        if len(response2)==0:
            break
        if i != 1:
            resp2.extend(response2)
        i += 1
    return render(request, 'info_ciudades.html', {'ciudades': resp, 'usuarios': resp2 ,'id': id})

def barra_busqueda(request):
    searched = request.GET['buscado']

    i = 1
    while True:
        response = requests.get(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/53372/users?q={searched}&_page={i}').json()
        if i == 1:
            resp = response
        if len(response)==0:
            break
        if i != 1:
            resp.extend(response)
        i += 1

    i=1
    while True:
        response2 = requests.get(f'https://us-central1-taller-integracion-310700.cloudfunctions.net/tarea-1-2021-2/53372/cities?q={searched}&_page={i}').json()
        if i == 1:
            resp2 = response2
        if len(response2)==0:
            break
        if i != 1:
            resp2.extend(response2)
        i += 1
    return render(request, 'resultado_busqueda.html', {'response': resp, 'response2':resp2, 'buscado': searched})
