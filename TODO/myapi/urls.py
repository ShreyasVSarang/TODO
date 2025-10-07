from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet) # Maps /api/items/ to the ItemViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]