seasons = {
    1: ("январь", "За окном падал белый снег"),
    2: ("февраль", "За окном падал белый снег"),
    3: ("март", "Птицы пели прекрасные песни"),
    4: ("апрель", "Птицы пели прекрасные песни"),
    5: ("май", "Птицы пели прекрасные песни"),
    6: ("июнь", "Солнце светило ярче чем когда-либо"),
    7: ("июль", "Солнце светило ярче чем когда-либо"),
    8: ("август", "Солнце светило ярче чем когда-либо"),
    9: ("сентябрь", "Урожай был невероятным"),
    10: ("октябрь", "Урожай был невероятным"),
    11: ("ноябрь", "За окном падал белый снег"),
    12: ("декабрь", "За окном падал белый снег"),
}

month = input("Введите номер месяца своего рождения: ")

try:
    month = int(month)
    if 1 <= month <= 12:
        name, description = seasons[month]
        print(f"Вы родились в {name}. {description}")
    else:
        print("Неверный номер месяца. Введите число от 1 до 12.")
except ValueError:
    print("Неверный формат ввода. Введите число от 1 до 12.")
