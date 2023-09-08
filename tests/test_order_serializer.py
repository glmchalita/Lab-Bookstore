import pytest
from productAPI.factories import ProductFactory
from orderAPI.models import Order
from orderAPI.factories import UserFactory, OrderFactory


@pytest.mark.django_db
def test_order_creation():
    # Crie um usuário usando a factory
    user = UserFactory()

    # Crie alguns produtos usando a factory
    product1 = ProductFactory()
    product2 = ProductFactory()

    # Crie um pedido com relação ao usuário e produtos usando a factory
    order = OrderFactory(user=user, product=[product1, product2])

    # Verifique se o pedido foi criado corretamente
    assert isinstance(order, Order)
    assert order.user == user
    assert product1 in order.product.all()
    assert product2 in order.product.all()


@pytest.mark.django_db
def test_order_product_addition():
    # Crie um usuário usando a factory
    user = UserFactory()

    # Crie alguns produtos usando a factory
    product1 = ProductFactory()
    product2 = ProductFactory()

    # Crie um pedido com relação ao usuário usando a factory
    order = OrderFactory(user=user)

    # Adicione produtos ao pedido
    order.product.add(product1, product2)

    # Verifique se os produtos foram adicionados corretamente ao pedido
    assert product1 in order.product.all()
    assert product2 in order.product.all()
