from django.shortcuts import render
from django.db.models import Q
from .models import News, Rahbariyat


def home(request):
    news = News.objects.all().order_by("-created_at")
    return render(request, "main/home.html", {"news": news})


def search(request):
    query = request.GET.get("q")
    results = []

    if query:
        results = News.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).order_by("-created_at")

    return render(request, "main/search.html", {
        "query": query,
        "results": results
    })


def rahbariyat(request):
    director = Rahbariyat.objects.filter(position='director').first()
    deputies = Rahbariyat.objects.filter(position='deputy')

    return render(request, "main/rahbariyat.html", {
        "director": director,
        "deputies": deputies,
    })

from .models import Oqituvchi

def oqituvchilar(request):
    oqituvchilar = Oqituvchi.objects.all().order_by("-created_at")
    return render(request, "main/oqituvchilar.html", {
        "oqituvchilar": oqituvchilar
    })

def tikuvchi(request):
    return render(request, 'main/tikuvchi.html')
    
def avtomobil_shasse(request):
    return render(request, 'main/avtomobil_shasse.html')

def elektromontyor(request):
    return render(request, 'main/elektromontyor.html')

def payvandlovchi(request):
    return render(request, 'main/payvandlovchi.html')

def sartarosh(request):
    return render(request, 'main/sartarosh.html')

def traktorchi_mashinist(request):
    return render(request, 'main/traktorchi_mashinist.html')

def kompyuter_tizimlari(request):
    return render(request, 'main/kompyuter_tizimlari.html')
