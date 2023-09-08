from rest_framework.viewsets import ModelViewSet

from productAPI.models import Product
from productAPI.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
