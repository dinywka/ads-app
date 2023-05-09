from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    categories = [
        {'id': 1, 'title': "Электроника", 'url': "electro", 'image': "imd.jpeg"},
        {'id': 2, 'title': "Ремонт", 'url': "remont", 'image': "imd.jpeg"},
        {'id': 3, 'title': "Детское", 'url': "det", 'image': "imd.jpeg"},
        {'id': 4, 'title': "Сувениры", 'url': "suv", 'image': "imd.jpeg"},
    ]
    return render(request, 'home.html',
                  context={'data': "Python", 'categories': categories})

def get_json(request):
    return JsonResponse(data={"name": "Dina"}, safe=False)