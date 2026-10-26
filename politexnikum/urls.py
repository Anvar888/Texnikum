from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.shortcuts import redirect
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # ⭐ VERY IMPORTANT
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
