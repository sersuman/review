from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register('product', ProductViewSet, basename='Product')
router.register('image', ImageViewSet, basename='Image')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('',include(router.urls)),
]

# To make Django development server serve media we need to add a URL pattern in urls.py file
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    