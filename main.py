def punkt_1():
# Введіть назву товару: Хліб
# Введіть кількість: 2
# Введіть ціну за одиницю: 25    

    return
def punkt_2():
    return
def punkt_3():
    return
def punkt_4():
    return
def punkt_5():
    return


def main():
    print("🛒 Вітаю у менеджері покупок! ")
    while True:
        print('''
    Меню:
    1. Додати покупку
    2. Переглянути список
    3. Порахувати загальну суму
    4. Зберегти у файл
    5. Завантажити з файлу
    6. Вихід
            ''')

        punkt_menu = int(input("Ваш вибір: "))
        match punkt_menu:
            case 1:
                punkt_1()
                continue
            case 2:
                punkt_2()
                continue
            case 3:
                punkt_3()
                continue
            case 4:
                punkt_4()
                continue
            case 5:
                punkt_5()
                continue
            case 6:
                break    

main()
