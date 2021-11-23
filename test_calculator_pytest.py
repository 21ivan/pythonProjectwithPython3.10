import pytest
from pyTests.applications.calculator import calculator


def test_plus():
    assert calculator('2+2') == 4


def test_minus():
    assert calculator('4-2') == 2


def test_multiple():
    assert calculator('3 * 2') == 6


def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('adidas')
    assert ('Вираз повинен містити хоча б один знак (+-/*)' == error.value.args[0])


def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator('2+4*5')
    assert ('Вираз повинен містити 2 цілі числа і 1 знак' == error.value.args[0])


def test_ints():
    with pytest.raises(ValueError) as error:
        calculator('2,0+4*5')
    assert ('Вираз повинен містити 2 цілі числа і 1 знак' == error.value.args[0])


def test_strings():
    with pytest.raises(ValueError) as error:
        calculator('a+b')
    assert ('Вираз повинен містити 2 цілі числа і 1 знак' == error.value.args[0])


if __name__ == '__main__':
    pytest.main()
