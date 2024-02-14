import json
import os
from typing import Union

import pytest

RESOURCE_JSON = "products_response.json"


def load_path(file_path: str, file_name: str) -> str:
    path, _ = os.path.split(file_path)
    return os.path.join(path, file_name)


def load_json(filepath: str, encoding: str = None) -> Union[dict, list]:
    with open(filepath, "r", encoding=encoding) as f:
        return json.loads(f.read())


def load_json_path(
    file_path: str, file_name: str, encoding: str = None
) -> Union[dict, list]:
    return load_json(load_path(file_path, file_name), encoding=encoding)


@pytest.fixture(scope="module")
def load_json_file(request):
    return load_json_path(__file__, f"resources/{RESOURCE_JSON}", "utf-8")
