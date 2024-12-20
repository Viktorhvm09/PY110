from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def datetime_view(request):
    if request.method == "GET":
        # data = datetime.now()
        data = datetime.now().strftime("%x %X")
    return HttpResponse(data)
