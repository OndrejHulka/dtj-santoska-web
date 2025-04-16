from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def historie(request):
    return render(request, 'historie.html')

def aktuality(request):
    return render(request, 'aktuality.html')

def areal(request):
    return render(request, 'areal.html')

def plan(request):
    return render(request, 'plan.html')

def probehle_akce(request):
    return render(request, 'probehleakce.html')

def kontakt(request):
    return render(request, 'kontakt.html')
