from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("search/", views.search, name="search"),   # 👈 MUHIM
    path("rahbariyat/", views.rahbariyat, name="rahbariyat"),
    path("oqituvchilar/", views.oqituvchilar, name="oqituvchilar"),
    path('tikuvchi/', views.tikuvchi, name='tikuvchi'),
    path('avtomobil-shasse/', views.avtomobil_shasse, name='avtomobil_shasse'),
    path('elektromontyor/', views.elektromontyor, name='elektromontyor'),
    path('payvandlovchi/', views.payvandlovchi, name='payvandlovchi'),
    path('sartarosh/', views.sartarosh, name='sartarosh'),
    path('traktorchi-mashinist/', views.traktorchi_mashinist, name='traktorchi_mashinist'),
    path('kompyuter-tizimlarida-dasturlash/', views.kompyuter_tizimlari, name='kompyuter_tizimlari'),
    path(
    "robots.txt",
    TemplateView.as_view(
        template_name="robots.txt",
        content_type="text/plain"
    ),
),
]
