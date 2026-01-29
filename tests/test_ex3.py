
# testing User Factory from factories.py
import pytest
from django.contrib.auth.models import User
from core.app1 import models


@pytest.mark.django_db
def test_user_factory_creation(user_factory):
    user = user_factory.build()
    count = User.objects.count()
    print(f"Number of users in database: {count}")

    # act Phase: Create a user using the UserFactory.
    print(f"Creating user with UserFactory{user_factory.username}")
    # assert Phase: Verify the user was created correctly.
    assert True
    assert user.username == user_factory.username
    assert user.is_staff == user_factory.is_staff
    assert user.pk is None  # since we used build(), not create()
    assert User.objects.count() == count  # No new user should be in DB


@pytest.mark.django_db
def test_product_factory_creation(db, product_factory):
    product = product_factory.create()
    count = models.Product.objects.count()
    print(f"Number of products in database: {count}")

    # act Phase: Create a product using the ProductFactory.
    print(f"Creating product with ProductFactory{product_factory.title}")
    # assert Phase: Verify the product was created correctly.
    assert True
    assert product.title == product_factory.title
    assert product.description == product_factory.description
    assert product.slug == product_factory.slug
    assert product.regular_price == product_factory.regular_price
    assert product.discount_price == product_factory.discount_price
    assert product.pk is not None  # since we used create(), not build()
    assert models.Product.objects.count() == count  # No new user should be in DB
