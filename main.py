import time

endings = []
person = {"name1": "Гачи бой1", "name2": "Гачи бой2"}
name1 = person["name1"]
name2 = person["name2"]

def introduction():
    print("Добро пожаловать в игру 'Путь к свободе черных братьев'")
    time.sleep(0.5)
    print("Вы начнете свою историю как раб.")
    time.sleep(0.5)
    print("Ваша цель - стать свободным и освободить своих братьев.")
    time.sleep(0.5)

name = input("Ваше имя: ")

def chapter_one():
    print("\nГлава 1: Первый шаг к свободе")
    time.sleep(1)
    print("Вы находитесь в рабской клетке, где вас держат в плену.")
    time.sleep(1)
    print("У вас есть два варианта:")
    time.sleep(1)
    choice = input("1. Попробовать сбежать через окно.\n2. Подождать и надеяться на лучшее.\nВыберите действие (1/2): ")

    if choice == "1":
        print("Вы решаете попробовать сбежать через окно.")
        time.sleep(1)
        print("У вас не получается. Вас поймали и назначили наказание в виде 50 ударов плетью, вы умерли от болевого шока.")
        time.sleep(1)
        game_over()
    elif choice == "2":
        print("Вы решаете подождать и надеяться на лучшее.")
        time.sleep(1)
        print("Через несколько дней вы замечаете, что дверь клетки не заперта.")
        time.sleep(1)
        chapter_two()

def chapter_two():
    global name
    print("\nГлава 2: Путь к свободе")
    print(f"Вы выходите из клетки и оказываетесь в большом здании. Вас зовут {name}.")
    print("Ваш следующий шаг:")
    choice = input("1. Попробовать найти своих братьев.\n2. Попытаться скрыться и выбраться на улицу.\nВыберите действие (1/2): ")

    if choice == "1":
        print("Вы решаете найти своих братьев.")
        print(f"Вы идете по коридору на корточках и вдруг видите 2х накаченных мужиков в латексном костюме. {name1} и {name2}")
        fight_choice = input("Что вы решаете сделать?\n1. Сразиться с ними.\n2. Отступить.\nВыберите действие (1/2): ")

        if fight_choice == "1":
            print("Вы решаете сразиться с ними.")
            print(f"{name1} ЧТО СЕБЕ ПОЗВОЛЯЕТ ЭТОТ ФАКИНГ СЛЭЙВ БРАТЕЦ?")
            print(f"{name2} сейчас мы как ДЭНЖИОН МАСТЕР покажему этому слейв фистинг каминг")
            print("*Пока они использовали неизвестенные вам термины по типу *фистинг*, *гив ми юр пасворд* и *we we* ")
            print(f"Вы наносите первый удар ЛОУ КИК прямо по яицам 1 мужику, но он даже не шолохнулся ")
            print(f"{name1} Сынуля я в качалке и не такое терпел. *Звук удара кулака который преодолел звуковой барьер*")
            print("Вы отлетели на несколько метров назад пробив стену прямо там где сидели в заперти ваши братья")
            print("*голос грозного брата* Йоу нигга ватафак ара ю доинг зис плейс * другой голос брата* говори по русский даун")
            print(f"Вы весь в крови, но на издыхание показывайте пальцем на 2 мужиков, мужики увидев орду черных братьев сбежали как СЛЭЙВ")
            print(f"{name} бро ты лучший, спасибо что спас *звуки из толпы* ГИП ГИП УРАААААААААААААААААААААА")
            win_game2()
        elif fight_choice == "2":
            print("Вы решаете отступить.")
            print("Вы чувствуете негативную энергию сзади и оборачиваетесь, но уже поздно странный мужик в маске был в кроксах и без труда вас догнал")
            print("Я не буду говорить что было дальше, жанр не подходит")
            game_over()
    elif choice == "2":
        print("Вы решаете скрыться и выбраться на улицу.")
        print("Вы находите выход и попадаете на свободу.")
        win_game1()

def chapter_three():
    print("\nГлава 3: Новый выбор")
    print("Теперь, когда вы свободны, у вас есть несколько важных решений.")
    print("Ваши варианты:")
    choice = input("1. Решить вернуться и освободить еще больше братьев.\n2. Попробовать начать новую жизнь в другом городе.\nВыберите действие (1/2): ")

    if choice == "1":
        print("Вы решаете вернуться и освободить еще больше братьев.")
        print("Ваша мужественность и решимость помогают освободить еще множество братьев, и вы становитесь настоящим героем.")
        win_game3()
    elif choice == "2":
        print("Вы решаете начать новую жизнь в другом городе.")
        print("Вы находите работу, находите новых друзей и начинаете жизнь, полную надежды и возможностей.")
        win_game4()
def win_game1():
    print(
        "\nПоздравляем! Вы стали свободным, но вы теперь одиноки, а ваши братьям придется влачить свою жизнь в несправедливом мучении")
    endings.append("Одинокая свобода...")
    play_again = input("Хотите начать заново? (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

def win_game2():
    print("\nПоздравляем! Вы стали свободным вмести со своими братьями")
    endings.append("Свобода с братьями")
    play_again = input("Хотите начать заново? (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

def win_game3():
    print("\nПоздравляем! Вы стали настоящим героем, освободив еще множество братьев.")
    endings.append("Герой освободителя")

    play_again = input("Хотите начать заново? (если вы прошли главу пишите нет) (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

def win_game4():
    print("\nПоздравляем! Вы начали     новую жизнь и нашли свое место в мире.")
    endings.append("Новая жизнь")

    play_again = input("Хотите начать заново? (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

def game_over():
    print("\nИгра завершена. Вы проиграли.")
    endings.append("Проигрыш")
    play_again = input("Хотите начать заново? (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

def start_game():
    introduction()
    chapter_one()

if __name__ == "__main__":
    start_game()

if endings:
    print("\nРазные концовки игры:")
    for i, ending in enumerate(endings):
        print(f"{i + 1}. {ending}")
