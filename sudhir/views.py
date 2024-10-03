from django.shortcuts import render
from .models import ChaiVariety
# Create your views here.

def all_sudhir(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'sudhir/all_sudhir.html',{'chais': chais})