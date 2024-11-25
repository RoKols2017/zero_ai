a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

if (a < c) and (a < b):
    min_num = "a"
elif (b < a) and (b < c):
    min_num = "b"
else:
    min_num = "c"

print(f"Меньшее число {min_num}")