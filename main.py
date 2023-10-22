import time

endings = []

def introduction():
    print("Добро пожаловать в игру 'Путь к свободе черных братьев'")
    time.sleep(0.5)
    print("Вы начнете свою историю как раб.")
    time.sleep(0.5)
    print("Ваша цель - стать свободным и освободить своих братьев.")
    time.sleep(0.5)

print(f"Ваш рабовладелец назвал вас {input('Введите имя ')}")

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
    print("\nГлава 2: Путь к свободе")
    time.sleep(1)
    print("Вы выходите из клетки и оказываетесь в большом здании.")
    time.sleep(1)
    print("Ваш следующий шаг:")
    time.sleep(1)
    choice = input(
        "1. Попробовать найти своих братьев.\n2. Попытаться скрыться и выбраться на улицу.\nВыберите действие (1/2): ")

    if choice == "1":
        print("Вы решаете найти своих братьев.")
        time.sleep(1)
        print("Вы находите клетки с другими братьями и освобождаете их. Теперь вы свободны и решайтесь мигрировать в другую страну, где вам будут рады.")
        time.sleep(1)
        win_game2()
    elif choice == "2":
        print("Вы решаете скрыться и выбраться на улицу.")
        time.sleep(1)
        print("Вы находите выход и попадаете на свободу.")
        time.sleep(1)
        win_game1()

def game_over():
    print("\nИгра окончена. Вы не смогли стать свободным.")
    endings.append("Bad ending")
    play_again = input("Хотите начать заново? (да/нет): ")
    if play_again.lower() == "да":
        start_game()
    else:
        print("Спасибо за игру!")

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

def start_game():
    introduction()
    chapter_one()

if __name__ == "__main__":
    start_game()

if endings:
    print("\nРазные концовки игры:")
    for i, ending in enumerate(endings):
        print(f"{i + 1}. {ending}")
