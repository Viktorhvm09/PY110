from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from .models import DATABASE
from logic.services import filtering_category

def products_view(request):
    if request.method == "GET":
        id = request.GET.get('id')
        if id:
            for i, values in DATABASE.items():
                if int(id) == values['id']:
                    return JsonResponse(DATABASE[i], json_dumps_params={'ensure_ascii': False,
                                                             'indent': 4})
            return HttpResponseNotFound("Данного продукта нет в базе данных")
        category_key = request.GET.get("category")
        data = None
        if ordering_key := request.GET.get("ordering"):
            if request.GET.get("reverse") and request.GET.get("reverse").lower() == 'true':
                data = filtering_category(DATABASE, category_key, ordering_key, reverse=True)
            else:
                data = filtering_category(DATABASE, category_key, ordering_key, reverse=False)
        else:
            data = filtering_category(DATABASE, category_key)
        if data:
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                             'indent': 4}, safe=False)
        return JsonResponse(DATABASE, json_dumps_params={'ensure_ascii': False,
                                                             'indent': 4})

def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ

def products_page_view(request, page):
    if request.method == "GET":
        if isinstance(page, str):
            for data in DATABASE.values():
                if data['html'] == page:
                    with open(f'store/products/{page}.html', encoding="utf-8") as f:
                        return HttpResponse(f.read())
        elif isinstance(page, int):
            data = DATABASE.get(str(page))
            if data:
                with open(f'store/products/{data["html"]}.html', encoding="utf-8") as f:
                    return HttpResponse(f.read())
        return HttpResponse(status=404)