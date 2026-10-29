from django.urls import path
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import reverse
from . import views
class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            "home",
            "search",
            "rahbariyat",
            "oqituvchilar",
            "tikuvchi",
            "avtomobil_shasse",
            "elektromontyor",
            "payvandlovchi",
            "sartarosh",
            "traktorchi_mashinist",
            "kompyuter_tizimlari",
        ]

    def location(self, item):
        return reverse(item)


sitemaps = {
    "pages": StaticViewSitemap,
}
urlpatterns = [
    path(
        "robots.txt",
        lambda request: HttpResponse(
            "User-agent: *\nAllow: /\n\nSitemap: https://qiziltepa-2sontexnikum.uz/sitemap.xml\n",
            content_type="text/plain"
        ),
    ),
    path(
    "sitemap.xml",
    sitemap,
    {"sitemaps": sitemaps},
    name="django.contrib.sitemaps.views.sitemap",
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
