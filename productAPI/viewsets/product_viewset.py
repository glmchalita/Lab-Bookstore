from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from productAPI.models import Product
from productAPI.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
