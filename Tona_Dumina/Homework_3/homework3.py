import pytest

#1.Пример с использованием списка параметров


@pytest.mark.parametrize("first_name,second_name", [(1, 2, 'max','test'), ('testing', 3)])
def test_example(first_name, second_name):
    print(first_name)
    print(second_name)
 # [missing-final-newline]
