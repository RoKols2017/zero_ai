num_min = int(input("Введите начало диапазона: "))
num_max = int(input("Введите конец диапазона: "))

for i in range(num_min, num_max + 1):
    if i % 2 == 0:
        print(i)
