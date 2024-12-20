from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE

def products_view(request):
    if request.method == "GET":
        # return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
        #                                          'indent': 4})
        id = request.GET.get('id')


        for i, values in DATABASE.items():
            if id == values.values('id'):
                return HttpResponse(DATABASE.values(i))
            elif id != values.values('id'):
                return HttpResponseNotFound("Данного продукта нет в базе данных")
            return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})

def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ