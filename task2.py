def check_month(month: int):
    if month >= 1 and month <= 12:
        if month == 12 or month <= 2:
            result = "Зима"
        elif month > 2 and month <= 5:
            result = "Весна"
        elif month > 5 and month < 9:
            result = "Лето"
        else:
            result = "Осень"
    else:
        result = "Некорректный номер месяца"

    return result


if __name__ == '__main__':
    # Этот код менять не надо
    season = check_month(1)
    assert season == 'Зима', "Ответ должен быть Зима"
    print(f"1 месяц время года: {season}")
    season = check_month(4)
    assert season == 'Весна', "Ответ должен быть Весна"
    print(f"4 месяц время года: {season}")
    season = check_month(18)
    assert season == "Некорректный номер месяца", "Ответ должен быть 'Некорректный номер месяца'"
    print(f"18 месяц: {season}")