a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
znak = input("Введите знак арифметического действия (+, -, *, /) : ")

if znak == "+":
    print("Сумма чилел равна", a + b)
elif znak == "-":
    print(a - b)
elif znak == "*":
    print(a * b)
elif znak == "/":
    if b == 0:
        print("Деление на 0")
    else:
        print(a / b)
else:
    print("Неверный знак")
