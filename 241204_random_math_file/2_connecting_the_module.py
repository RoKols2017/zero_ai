#  Создание модуля с функциями арифметики
# Создайте модуль arithmetic.py, который будет содержать 4 функции: сложение, вычитание, умножение и деление.
# Импортируйте модуль в другой файл Python и выполните каждую из функций с произвольными аргументами.
import arithmetic

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print(f"Сумма чисел: {arithmetic.add(a, b)}")
print(f"Разность чисел: {arithmetic.sub(a, b)}")
print(f"Произведение чисел: {arithmetic.mul(a, b)}")
if b == 0:
    print("Деление на 0 невозможно")
else:
    print(f"Частное чисел: {arithmetic.div(a, b)}")

