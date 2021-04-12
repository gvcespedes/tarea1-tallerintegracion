from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
import requests

# Create your views here.

def home(request):
    response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    response2 = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    temps = []
    temps2= []
    for i in response:
        if i['season'] not in temps:
            temps.append(i['season'])
    for i in response2:
        if i['season'] not in temps2:
            temps2.append(i['season'])
    
    return render(request, 'lista_temporadas.html', {'temps': temps, 'temps2': temps2})

def lista_episodios(request, serie, temporada):
    if serie == 'breakingbad':
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
    else:
        response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
    return render(request, 'lista_titulos.html', {'response': response, 'temporada': temporada})

def episodio_especifico(request, episodio):
    response = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/episodes/{episodio}').json()
    return render(request, 'info_especifica.html', {'response': response})
   
def personaje_especifico(request, nombre):
    response = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={nombre}').json()
    response2 = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/quote?author={nombre}').json()
    return render(request, 'info_personaje.html', {'response': response, 'response2': response2})

def barra_busqueda(request):
    searched = request.GET['buscado']
    response = requests.get(f'https://tarea-1-breaking-bad.herokuapp.com/api/characters?name={searched}').json()
    return render(request, 'resultado_busqueda.html', {'response': response, 'buscado': searched})

