import random

# Функція запитує, скільки спроб хоче користувач
def ask_attempts():
    while True:
        answer = input("Скільки спроб ви хочете? Введіть число або просто натисніть Enter для виходу: ")
        if answer == "":
            exit("Гру завершено користувачем.")
        if answer.isdigit() and int(answer) > 0:
            return int(answer)
        print("Некоректне число. Спробуйте ще.")

# Функція запитує здогад користувача
def get_guess():
    answer = input("Ваша здогадка? (Enter — для виходу): ")
    if answer == "":
        exit("Гру завершено користувачем.")
    if answer.isdigit():
        return int(answer)
    print("Це не число. Спробуйте ще раз.")
    return get_guess()

# Основна функція гри
def play_game():
    print("Вітаю! Я загадав число від 1 до 100.\nСпробуйте вгадати його.")

    attempts = ask_attempts()
    secret_number = random.randint(1, 100)

    for _ in range(attempts):
        guess = get_guess()
        if guess < secret_number:
            print("Занадто маленьке!")
        elif guess > secret_number:
            print("Занадто велике!")
        else:
            print(f"Ви вгадали! Це число {secret_number}.")
            break
    else:
        print(f"Спроби закінчились. Загадане число було: {secret_number}.")

    ask_retry()

# Функція повторної гри
def ask_retry():
    answer = input("Хочете спробувати ще раз? (так/ні): ").strip().lower()
    if answer == "так":
        play_game()
    else:
        print("Дякую за гру!")

# Запуск гри
if __name__ == "__main__":
    play_game()
