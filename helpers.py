from collections import Counter
from typing import Union


def assert_compare_items(testing_items, expected_items):
    """
    Compare two lists of items and raise an assertion error if they are not equal.
    """

    def get_error_message():
        extra_items = set(testing_items).difference(set(expected_items))
        if extra_items:
            return f"Extra items we did not expect = {extra_items}"

        missing_items = set(expected_items).difference(set(testing_items))
        if missing_items:
            return f"Items we expected but did not get = {missing_items}"

        return f"\nReceived items = {testing_items}\nexpected items = {expected_items}"

    is_equal = Counter(testing_items) == Counter(expected_items)
    assert is_equal, get_error_message()


def get_products(json_response):
    return json_response.get("products")


def get_product_names(json_response) -> list:
    return [product.get("name") for product in json_response.get("products")]


def get_products_by_threshold_price(
    json_response, threshold_price: Union[float, int]
) -> list:
    if not isinstance(threshold_price, (float, int)):
        raise TypeError(
            f"Please provide either a float or integer, not {type(threshold_price)}"
        )
    return [
        product
        for product in json_response.get("products")
        if product.get("price") >= threshold_price
    ]
