import pytest


# 1. Пример с использованием списка параметров
@pytest.mark.parametrize("input_value, expected", [(1, 2), (2, 3), (3, 4)])
def test_increment_function(input_value, expected):
    assert input_value + 1 == expected


# 2. Пример с использованием параметризации по именованным аргументам
@pytest.mark.parametrize("input_value, expected", [
    (1, 2),
    pytest.param(2, 4, marks=pytest.mark.xfail(reason="Expected to fail"))
])
def test_double_function(input_value, expected):
    assert input_value * 2 == expected


# 3. Пример с динамической генерацией параметров
@pytest.mark.parametrize("input_value", range(5))
def test_square_function(input_value):
    assert input_value ** 2 == input_value * input_value


# 4. Пример с использованием параметризации по словарю
@pytest.mark.parametrize("name, age", [
    ("Alice", 25),
    ("Bob", 30),
    ("Eve", 28)
])
def test_person_age(name, age):
    assert age > 20


# 5. Пример с использованием параметризации по различным типам входных данных
@pytest.mark.parametrize("input_value, expected", [
    (1, "TypeError"),
    ("hello", "hello world"),
    ([1, 2, 3], [1, 2, 3, 4])
])
def test_append_function(input_value, expected):
    if isinstance(input_value, list):
        result = input_value + [4]
    elif isinstance(input_value, str):
        result = input_value + " world"
    else:
        pytest.fail("Invalid input type")
    assert result == expected


# 6. Пример использования параметризации с использованием фабричных функций
def data_provider():
    return [
        (1, 2),
        (2, 3),
        (3, 4)
    ]


@pytest.mark.parametrize("input_value, expected", data_provider())
def test_increment_function_with_provider(input_value, expected):
    assert input_value + 1 == expected


# 7. Пример с использованием параметризации с фильтрацией параметров
@pytest.mark.parametrize("input_value", range(10), ids=lambda x: f"input={x}")
def test_even_number(input_value):
    if input_value % 2 != 0:
        pytest.skip("Skipping the test for odd numbers")
    assert input_value % 2 == 0
