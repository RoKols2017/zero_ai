def bank(a, years):
    x = 0
    for i in range(1, years+1):
        a = 1.1 * a
    return (a)

summa = float(input("Введите сумму вклада: "))
srok = int(input("Введите срок вклада: "))

y = bank(summa, srok)
print(y)