from django.shortcuts import render
import sys
from django.urls import resolve

# Create your views here.
def home_view(request):
    app_name = sys.modules[resolve(request.path_info).func.__module__].__package__
    context = {}
    return render(request, f'{app_name}/home.html', context, status=200)

def index_view(request):
    app_name = sys.modules[resolve(request.path_info).func.__module__].__package__
    context = {}
    return render(request, f'{app_name}/index.html', context, status=200)