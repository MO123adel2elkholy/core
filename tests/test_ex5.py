# premrize Fleds
import pytest


@pytest.mark.parametrize("title, category, description , slug , regular_price , discount_price , validity",  [
    ("Test Product 1", "Category 1", "Description for Test Product 1",
     "test-product-1", 100, 80, True),
    ("Test Product 2", "Category 2", "Description for Test Product 2",
     "test-product-2", 200, 160, False),
])
def test_product_fields(db, product_factory, title, category, description, slug, regular_price, discount_price, validity):
    product = product_factory.create(
        title=title,
        category__name=category,
        description=description,
        slug=slug,
        regular_price=regular_price,
        discount_price=discount_price
    )

    assert product.title == title
    assert product.category.name == category
    assert product.description == description
    assert product.slug == slug
    assert product.regular_price == regular_price
    assert product.discount_price == discount_price
    assert product.is_active == True
