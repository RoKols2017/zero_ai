def sum_range(start, end):
    x = 0
    for i in range(start, end+1):
        x += i
    return (x)

y = sum_range(1,5)
print(f"Сумма равна: {y}")

