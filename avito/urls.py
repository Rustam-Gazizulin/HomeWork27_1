from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ads import views
from ads.views import CategoryViewSet, AdViewSet
from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register('loc', LocationViewSet)
router.register('cat', CategoryViewSet)
router.register('ad', AdViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', views.root),

    path('selection/', include('ads.urls.selection_urls')),

    path('user/', include('users.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
