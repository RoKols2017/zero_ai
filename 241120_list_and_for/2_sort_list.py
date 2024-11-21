my_list = []

for i in range(3):
    my_list.append(i)

print(my_list)

for i in range(2):
    my_list.insert(0, i + 3)

print(my_list)

sorted_list = sorted(my_list, reverse=True)

print("Updated List:", sorted_list)