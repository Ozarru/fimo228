from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('designers/', include('designers.urls')),
    path('mannequins/', include('mannequins.urls')),
    path('shop/', include('shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
