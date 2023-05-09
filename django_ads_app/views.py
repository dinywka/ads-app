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

    vip_ads= [
        {'id': 1, 'seller': "Admin", 'title': "Книга", 'price': 1500.0, 'category': "electro", 'image': "imd.jpeg"},
        {'id': 2, 'seller': "User1", 'title': "Ноутбук", 'price': 1500.0, 'category': "electro", 'image': "imd.jpeg"},
        {'id': 3, 'seller': "User2", 'title': "Вентлятор", 'price': 1500.0, 'category': "electro", 'image': "imd.jpeg"},
        {'id': 4, 'seller': "User3", 'title': "Картина", 'price': 1500.0, 'category': "electro", 'image': "imd.jpeg"},
    ]

    return render(request, 'home.html',
                  context={'categories': categories, 'vip_ads': vip_ads})

def get_json(request):
    return JsonResponse(data={"name": "Dina"}, safe=False)

def login(request):
    return render(
        request, 'login.html'
    )