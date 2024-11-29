from django.contrib import admin # type: ignore
from django.urls import path , include # type: ignore

from core.views import index
from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls")),  # Mengarahkan ke core.urls
    path("user/", include("userauths.urls")),
    path('', index, name='index'),  # Mengarahkan ke core.views.index
]

# akses semua settings.py
# STATIC_URL && STATIC_ROOT
# MEDIA_URL && MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)