from django.shortcuts import render
from .models import Buyurtma, Chegirma

def buyurtma_list(request):
    buyurtmalar = Buyurtma.objects.all()
    return render(request, 'buyurtma_list.html', {'buyurtmalar': buyurtmalar})

def chegirma_list(request):
    chegirmalar = Chegirma.objects.all()
    return render(request, 'chegirma_list.html', {'chegirmalar': chegirmalar})
