import pytest

from helpers import (
    assert_compare_items,
    get_product_names,
    get_products_by_threshold_price,
    get_products,
)

EXPECTED_PRODUCT_NAMES = ["Pizza", "Sushi", "Burger", "Pad Thai"]


def test_get_product_names(load_json_file):
    actual_product_names = get_product_names(load_json_file)
    actual_products = get_products(load_json_file)
    assert_compare_items(actual_product_names, EXPECTED_PRODUCT_NAMES)
    assert len(actual_product_names) == len(actual_products)


@pytest.mark.parametrize(
    "threshold, expected_data",
    [
        (
            0,
            [
                {"id": 1, "name": "Pizza", "category": "Italian", "price": 12.99},
                {"id": 2, "name": "Sushi", "category": "Japanese", "price": 24.99},
                {"id": 3, "name": "Burger", "category": "American", "price": 8.99},
                {"id": 4, "name": "Pad Thai", "category": "Thai", "price": 14.99},
            ],
        ),
        (
            14.99,
            [
                {"id": 2, "name": "Sushi", "category": "Japanese", "price": 24.99},
                {"id": 4, "name": "Pad Thai", "category": "Thai", "price": 14.99},
            ],
        ),
        (30, []),
    ],
    ids=["returns all items", "returns only equal 14.99 or more", "returns empty list"],
)
def test_get_products_by_threshold(load_json_file, threshold, expected_data):
    assert get_products_by_threshold_price(load_json_file, threshold) == expected_data


@pytest.mark.parametrize("input_data", ["20", None])
def test_get_products_by_threshold_with_incorrect_input_type(
    load_json_file, input_data
):
    with pytest.raises(TypeError):
        get_products_by_threshold_price(load_json_file, input_data)
