import pytest
from task1 import check_age
from task2 import check_month
from task3 import get_cost


@pytest.mark.parametrize("age, expected", [
    (17, 'Доступ запрещён'),
    (18, 'Доступ разрешён'),
    (20, 'Доступ разрешён'),
    (16, 'Доступ запрещён')
])
def test_check_age(age, expected):
    assert check_age(age) == expected


@pytest.mark.parametrize("month, expected", [
    (1, "Зима"),
    (5, "Весна"),
    (7, "Лето"),
    (9, "Осень"),
    (12, "Зима"),
    (13, "Некорректный номер месяца")
])
def test_check_month(month, expected):
    assert check_month(month) == expected


@pytest.mark.parametrize("weight, expected", [
    (5, 'Стоимость доставки: 200 руб.'),
    (10, 'Стоимость доставки: 200 руб.'),
    (15, 'Стоимость доставки: 500 руб.'),
    (0, 'Стоимость доставки: 200 руб.')
])
def test_get_cost(weight, expected):
    assert get_cost(weight) == expected
