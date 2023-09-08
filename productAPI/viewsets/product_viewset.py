from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from productAPI.models import Product
from productAPI.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_querset(self):
        return Product.objects.all()
