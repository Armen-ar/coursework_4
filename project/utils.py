import json
from typing import Union


def read_json(filename: str, encoding: str = "utf-8") -> Union[list, dict]:
    """
    Метод открывает json файл для чтения
    """
    with open(filename, encoding=encoding) as f:
        return json.load(f)
