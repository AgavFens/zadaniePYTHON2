import json
import csv
import os

endings = []

def save_game(data):
    with open('save_game.json', 'w') as save_file:
        json.dump(data, save_file)

def load_game():
    try:
        with open('save_game.json', 'r') as save_file:
            data = json.load(save_file)
        return data
    except FileNotFoundError:
        return None

def write_to_csv(data):
    with open('game_data.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(data)

def introduction():
    print("Добро пожаловать в игру 'Путь к свободе черных братьев'")
    print("Вы начнете свою историю как раб.")
    print("Ваша цель - стать свободным и освободить своих братьев.")

name = input('Введите имя персонажа: ')

def chapter_one():
    print("\nГлава 1: Первый шаг к свободе")
    print("Вы находитесь в рабской клетке, где вас держат в плену.")
    print("У вас есть два варианта:")
    choice = input("1. Попробовать сбежать через окно.\n2. Подождать и надеяться на лучшее.\nВыберите действие (1/2): ")

    if choice == "1":
        print("Вы решаете попробовать сбежать через окно.")
        print("Вы сиганули с окна и пока вы летели вниз вы поняли что спрыгнули с 16 этажа вниз (по вашим расчетам).")
        print("*Звуки сломанных костей* Вы сломали себе ноги, но вы не унывайте ведь выход совсем рядом.")
        print("*Неожиданный звук выстрела* Вы поняли что упали прямо на стрельбище и вас убили :(")
        game_over()
    elif choice == "2":
        print("Вы решаете подождать и надеяться на лучшее.")
        print("Через несколько дней вы замечаете, что дверь клетки не заперта.")
        chapter_two()

def chapter_two():
    print("\nГлава 2: Путь к свободе")
    print("Вы выходите из клетки и оказываетесь в большом здании.")
    print("Ваш следующий шаг:")
    choice = input("1. Попробовать найти своих братьев.\n2. Попытаться скрыться и выбраться на улицу.\nВыберите действие (1/2): ")

    if choice == "1":
        print("Вы решаете найти своих братьев.")
        print("Вы идете по коридору на корточках и вдруг видите 2х накаченных мужиков в латексном костюме. ")
        fight_choice = input("Что вы решаете сделать?\n1. Сразиться с ними.\n2. Отступить.\nВыберите действие (1/2): ")

        if fight_choice == "1":
            print("Вы решаете сразиться с ними.")
            print("*Голос мужика1* ЧТО СЕБЕ ПОЗВОЛЯЕТ ЭТОТ ФАКИНГ СЛЭЙВ БРАТЕЦ?")
            print("*Голос мужика2* сейчас мы как ДЭНЖИОН МАСТЕР покажему этому слейв фистинг каминг")
            print("*Пока они использовали неизвестенные вам термины по типу *фистинг*, *гив ми юр пасворд* и *we we* ")
            print("Вы наносите первый удар ЛОУ КИК прямо по яицам 1 мужику, но он даже не шолохнулся ")
            print("*Голос мужика1* Сынуля я в качалке и не такое терпел. *Звук удара кулака который преодолел звуковой барьер*")
            print("Вы отлетели на несколько метров назад пробив стену прямо там где сидели в заперти ваши братья")
            print("*голос грозного брата* Йоу нигга ватафак ара ю доинг зис плейс * другой голос брата* говори по русский даун")
            print("Вы весь в крови, но на издыхание показывайте пальцем на 2 мужиков, мужики увидев орду черных братьев сбежали как СЛЭЙВ")
            print(name + "бро ты лучший, спасибо что спас *звуки из толпы* ГИП ГИП УРАААААААААААААААААААААА")
            win_game2()
        elif fight_choice == "2":
            print("Вы решаете отступить.")
            print("Вы чувствуйте негативную энергию сзади и оборачиваетесь, но уже поздно странный мужик в маске был в кроксах и без труда вас догнал")
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

def game_over():
    print("\nИгра окончена. Вы не смогли стать свободным.")
    endings.append("Плохой конец")

    data = {
        "name": name,
        "chapter": 1
    }
    save_game(data)
    data = [name, "Плохой конец"]
    write_to_csv(data)

    play_again = input("Хотите начать заново? (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        delete_save = input("Хотите удалить сохранение? (да/нет): ")
        if delete_save.lower() == "да":
            try:
                os.remove('save_game.json')
            except FileNotFoundError:
                pass
        print("Спасибо за игру!")

def win_game1():
    print(
        "\nПоздравляем! Вы стали свободным, но вы теперь одиноки, а ваши братьям придется влачить свою жизнь в несправедливом мучении")
    endings.append("Одинокая свобода...")

    with open('endings.csv', mode='w', newline='') as endings_file:
        endings_writer = csv.writer(endings_file)
        endings_writer.writerow(endings)

    data = [name, "Одинокая свобода..."]
    write_to_csv(data)

    play_again = input("Хотите начать заново? (если вы прошли главу пишите нет) (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

def win_game2():
    print("\nПоздравляем! Вы стали свободным вмести со своими братьями")
    endings.append("Свобода с братьями")

    with open('endings.csv', mode='w', newline='') as endings_file:
        endings_writer = csv.writer(endings_file)
        endings_writer.writerow(endings)

    data = [name, "Свобода с братьями"]
    write_to_csv(data)

    play_again = input("Хотите начать заново? (если вы прошли главу пишите нет) (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

def win_game3():
    print("\nПоздравляем! Вы стали настоящим героем, освободив еще множество братьев.")
    endings.append("Герой освободителя")

    with open('endings.csv', mode='w', newline='') as endings_file:
        endings_writer = csv.writer(endings_file)
        endings_writer.writerow(endings)

    data = [name, "Герой освободителя"]
    write_to_csv(data)

    play_again = input("Хотите начать заново? (если вы прошли главу пишите нет) (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

def win_game4():
    print("\nПоздравляем! Вы начали новую жизнь и нашли свое место в мире.")
    endings.append("Новая жизнь")

    with open('endings.csv', mode='w', newline='') as endings_file:
        endings_writer = csv.writer(endings_file)
        endings_writer.writerow(endings)

    data = [name, "Новая жизнь"]
    write_to_csv(data)

    play_again = input("Хотите начать заново? (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

def start_game():
    introduction()
    saved_data = load_game()

    if saved_data:
        print("Вы нашли сохраненные данные. Хотите продолжить игру?")
        choice = input("1. Начать новую игру.\n2. Продолжить сохраненную игру.\nВыберите действие (1/2): ")

        if choice == "1":
            chapter_one()
            chapter_three()
        elif choice == "2":
            name = saved_data["name"]
            chapter = saved_data["chapter"]
            if chapter == 1:
                chapter_one()
            elif chapter == 2:
                chapter_two()
            elif chapter == 3:
                chapter_three()
    else:
        chapter_one()
        chapter_three()

if __name__ == "__main__":
    start_game()

if endings:
    print("\nРазные концовки игры:")
    for i, ending in enumerate(endings):
        print(f"{i + 1}. {ending}")
