from django.shortcuts import render

# Create your views here.

def index(request):
    peliculas = [
        {
            'titulo': 'Avatar 2',
            'imagen' : 'https://i.pinimg.com/236x/35/e3/81/35e3815780a3a38cce4481c7ca45e640.jpg',
        },
        {
            'titulo': 'Shazam 2',
            'imagen' : 'https://i.pinimg.com/236x/ca/c8/e0/cac8e0bbab8026b11effb9a8b84bd547.jpg',
        },
        {
            'titulo': 'Gato con Botas 2',
            'imagen' : 'https://i.pinimg.com/736x/32/61/82/3261829acb6a5563debbb9c9735b802a.jpg',
        }
    ]
    return render('')