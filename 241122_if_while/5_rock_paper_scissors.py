import random

game_list = ["Камень", "Ножницы", "Бумага"]
caunt_win_pc = 0
caunt_lose_pc = 0

print("Играем в игру: Камень, Ножницы, Бумага")
while True:
    print ("Для выбора введите")
    x = int(input("1 - Камень, 2 - Ножницы, 3 - Бумага: "))

    y = random.randint(1,3)
    print(f"Вы выбрали {game_list[x - 1]}, я выбрал {game_list[y - 1]}")

    if x == y:
        print("Ничья")
    elif x == 1 and y == 2:
        print("Вы победили")
        caunt_lose_pc += 1
    elif x == 2 and y == 3:
        print("Вы победили")
        caunt_lose_pc += 1
    elif x == 3 and y == 1:
        print("Вы победили")
        caunt_lose_pc += 1
    else:
        print("Вы проиграли")
        caunt_win_pc += 1

    print(f"Счет: Игрок {caunt_lose_pc}, РС {caunt_win_pc}")
    if caunt_lose_pc == 3 or caunt_win_pc == 3:
        break
