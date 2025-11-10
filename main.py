import csv

def add_item():
    name_produkt = input("Введіть назву товару: ").capitalize()
    count_produkt = int(input("Введіть кількість: "))
    price_produkt = float(input("Введіть ціну за одиницю: "))
    print(f"✅ {name_produkt} додано до списку!")
    return {"name": name_produkt, "count": count_produkt, "price": price_produkt}

def show_list(sh_lst):
    print("Ваш список покупок: ")
    for i, el in enumerate(sh_lst):
        print(f"{i + 1}. {el["name"]}- {el["count"]}шт за ціною {el["price"]}")
    return

def sum_total(sh_lst):
    sum = 0
    for el in sh_lst:
        sum += el["count"] * el["price"]
    return print(f"Поточна сума ваших покупок становить: {sum}")

def save_file(sh_lst, file_path):
    with open(file_path, mode="w") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        for elem in sh_lst:
            row = [elem["name"], elem["count"], elem["price"]]
            writer.writerow(row)
    return

def load_file(sh_lst, file_path):
    if sh_lst != []:
        ans = input("Додати дані до існуючого списку*(y/n)?")
        if ans == "n":
            ans = input("Ваш поточний список буде знищено(y/n)?")
            if ans == "":
                sh_lst = []
    with open(file_path) as csv_file:
        reader = csv.reader(csv_file, delimiter=";")
    for elem in reader:
        item = {
            "name": elem[0],
            "count": elem[1],
            "price": elem[3]
            }
        sh_lst.append(item)
    return sh_lst


def main():
    print("🛒 Вітаю у менеджері покупок! ")
    shopping_list = []
    file_path = './data/Shopping_list.csv'
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

        punkt_menu = int(input("Ваш вибір(1-6): "))
        match punkt_menu:
            case 1:
                shopping_list.append(add_item())
                answer = input("Перейти до меню (Y/N)?: ").lower()
                if answer == "n":
                    break
                continue
            case 2:
                show_list(shopping_list)
                answer = input("Перейти до меню (Y/N)?: ").lower()
                if answer == "n":
                    break
                continue
            case 3:
                sum_total(shopping_list)
                answer = input("Перейти до меню (Y/N)?: ").lower()
                if answer == "n":
                    break
                continue
            case 4:
                save_file(shopping_list,file_path)
                answer = input("Перейти до меню (Y/N)?: ").lower()
                if answer == "n":
                    break
                continue
            case 5:
                shopping_list = load_file(shopping_list, file_path)
                answer = input("Перейти до меню (Y/N): ").lower()
                if answer == "n":
                    break
                continue
            case 6:
                break   
            case _:
                print("Введено не вірні данні! Введіть 1-6")
                continue 

main()
