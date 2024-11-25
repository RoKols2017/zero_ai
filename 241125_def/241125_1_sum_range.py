def sum_range(start, end):
    x = 0
    for i in range(start, end+1):
        x += i
        print(f"Сумма равна: {x}")

sum_range(1,3)
