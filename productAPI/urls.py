from django.urls import path, include
from rest_framework import routers

from productAPI import viewsets

router = routers.SimpleRouter()
router.register(r'product', viewsets.ProductViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
