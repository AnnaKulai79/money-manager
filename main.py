def add_item():
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
    return {"name": name_produkt, "count": count_produkt, "price": price_produkt}

def show_list(sh_lst):
    if not sh_lst:
        print("\nВаш список покупок порожній")
        return    
    print("\nВаш список покупок: ")
    for i, el in enumerate(sh_lst):
        print(f"{i + 1}. {el["name"]}- {el["count"]}шт за ціною {el["price"]}")

def sum_total(sh_lst):
    sum = 0
    for el in sh_lst:
        sum += el["count"] * el["price"]
    return print(f"Поточна сума ваших покупок становить: {sum}")

def save_file(sh_lst, file_path):
    with open(file_path, "a") as f: # a ==> for appending
        for elem in sh_lst:
            f.write(f"{elem["name"]},{elem["count"]},{elem["price"]}\n")

def load_file(sh_lst, file_path):
    if sh_lst != []:
        ans = input("Додати дані до існуючого списку*(y/n)?")
        if ans == "n":
            ans = input("Ваш поточний список буде знищено(y/n)?").lower()
            if ans != "n":
                sh_lst = []
    sh_l = []
    with open(file_path, "r") as f: # r ==> open for reading
        for line in f:
            name, count, price = line.split(",")
            sh_l.append({
                "name": name,
                "count": count,
                "price": price,
                })
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
        except ValueError:
            print("\nВведено не вірні данні! Введіть 1-6")


main()
