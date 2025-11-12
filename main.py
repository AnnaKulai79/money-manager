import csv

def add_item():
    while True:
        data = input("Введіть дату у форматі дд-мм-рр: ").split("-")
        if len(data) == 3 and\
              len(data[0]) == len(data[1]) == len(data[2]) == 2 and\
              0 < int(data[0]) <= 31 and\
              0 < int(data[1]) <= 12  :
            data = "-".join(data)
            break
        else:
            print("Не вірний формат. Спробуй ще!")
    name_produkt = input("Введіть назву товару: ").capitalize()
    while True:
        try:
            count_produkt = int(input("Введіть кількість: "))
            break
        except Exception:
            print("Це не ціле число. Спробуй ще!")
    while True:
        try:
            price_produkt = float(input("Введіть ціну за одиницю: "))
            break
        except Exception:
            print("Це не число. Спробуй ще!")
    print(f"✅ {name_produkt} додано до списку!")
    return {"data": data, "name": name_produkt, "count": count_produkt, "price": price_produkt}

def show_list(sh_lst):
    if not sh_lst:
        print("\nВаш список покупок порожній.")
        return  

    answer = input("Відсортувати за датою (Y/N)?: ").strip().lower()
    sh_lst.sort(key=lambda x: x["data"])
    if answer == "y":
        while True:
            data = input("Введіть дату у форматі дд-мм-рр: ").split("-")
            if len(data) == 3 and\
                len(data[0]) == len(data[1]) == len(data[2]) == 2 and\
                0 < int(data[0]) <= 31 and\
                0 < int(data[1]) <= 12  :
                data = "-".join(data)
                break
            else:
                print("Не вірний формат. Спробуй ще!")

        filtered = [item for item in sh_lst if item["data"] == data]

        if filtered:
            print(f"\nВаш список покупок для дати {data}:")
            for i, el in enumerate(filtered, 1):
                print(f'{i}. {el["name"]} — {el["count"]} шт за ціною {el["price"]}')
            return
        else:
            print("\nТакої дати немає у списку. Буде показано увесь список.\n")

    previous_date = None
    print("\nУвесь список покупок:")
    for i, el in enumerate(sh_lst, 1):
        if el["data"] != previous_date:
            previous_date = el["data"]
            print(f"\nДата: {el['data']}")
        print(f'{i}. {el['name']} — {el['count']} шт за ціною {el['price']}')

def sum_total(sh_lst):
    sum = 0
    for el in sh_lst:
        sum += el["count"] * el["price"]
    return print(f"Поточна сума ваших покупок становить: {sum}")

def save_file(sh_lst, file_path):
    with open(file_path, "a", encoding="utf-8") as f: # a ==> for appending
        for elem in sh_lst:
            f.write(f'{elem["data"]},{elem["name"]},{elem["count"]},{elem["price"]}\n')
    print("Ваш список успішно збережено!")

def load_file(sh_lst, file_path):
    if sh_lst != []:
        ans = input("Додати дані до існуючого списку*(y/n)?")
        if ans == "n":
            ans = input("Ваш поточний список буде знищено(y/n)?").lower()
            if ans != "n":
                sh_lst = []
    sh_l = []
    with open(file_path, "r", encoding="utf-8") as f: # r ==> open for reading
        for line in f:
            data, name, count, price = line.split(",")
            sh_l.append({
                "data": data,
                "name": name,
                "count": int(count),
                "price": float(price),
                })
    print("Ваш список успішно зчитано з файлу!")
    return sh_l + sh_lst


def main():
    print("🛒 Вітаю у менеджері покупок! ")
    shopping_list = []
    file_path = './data/Shopping_list.txt'
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
        try:
            punkt_menu = int(input("Ваш вибір(1-6): "))
        except ValueError:
            print("\nВведено не вірні данні! Введіть 1-6")
            continue
        match punkt_menu:
            case 1:
                shopping_list.append(add_item())
                answer = input("Перейти до меню (Y/N)?: ").lower()
                if answer == "n":
                    break
            case 2:
                show_list(shopping_list)
                answer = input("Перейти до меню (Y/N)?: ").lower()
                if answer == "n":
                    break
            case 3:
                sum_total(shopping_list)
                answer = input("Перейти до меню (Y/N)?: ").lower()
                if answer == "n":
                    break
            case 4:
                save_file(shopping_list,file_path)
                answer = input("Перейти до меню (Y/N)?: ").lower()
                if answer == "n":
                    break
            case 5:
                shopping_list = load_file(shopping_list, file_path)
                answer = input("Перейти до меню (Y/N): ").lower()
                if answer == "n":
                    break
            case 6:
                break   
            case _:
                print("\nВведено не вірні данні! Введіть 1-6")
                continue 
if __name__ == "__main__":
    main()
