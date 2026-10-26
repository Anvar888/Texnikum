from django.contrib import admin
from .models import News, Rahbariyat, Oqituvchi


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)


@admin.register(Rahbariyat)
class RahbariyatAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "phone")
    list_filter = ("position",)
    search_fields = ("full_name",)


@admin.register(Oqituvchi)
class OqituvchiAdmin(admin.ModelAdmin):
    list_display = ("full_name", "subject", "phone")
    search_fields = ("full_name", "subject")
