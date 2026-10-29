
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path(
        "robots.txt",
        lambda request: HttpResponse(
            "User-agent: *\nAllow: /\n\nSitemap: https://qiziltepa-2sontexnikum.uz/sitemap.xml\n",
            content_type="text/plain"
        ),
    ),
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),
    path("rahbariyat/", views.rahbariyat, name="rahbariyat"),
    path("oqituvchilar/", views.oqituvchilar, name="oqituvchilar"),
    path("tikuvchi/", views.tikuvchi, name="tikuvchi"),
    path("avtomobil-shasse/", views.avtomobil_shasse, name="avtomobil_shasse"),
    path("elektromontyor/", views.elektromontyor, name="elektromontyor"),
    path("payvandlovchi/", views.payvandlovchi, name="payvandlovchi"),
    path("sartarosh/", views.sartarosh, name="sartarosh"),
    path("traktorchi-mashinist/", views.traktorchi_mashinist, name="traktorchi_mashinist"),
    path("kompyuter-tizimlarida-dasturlash/", views.kompyuter_tizimlari, name="kompyuter_tizimlari"),
]
