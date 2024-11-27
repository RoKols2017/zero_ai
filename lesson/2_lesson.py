# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются
# слева направо и справа налево

def reverse_string(string):
    reverse_string = ""
    for i in string:
        reverse_string = i + reverse_string
    return(reverse_string)

def srez(string):
    return(string[::-1])

str_1 = "искатьтакси"

print(reverse_string(str_1))
print(srez(str_1))
print(f"Длиа строки {len(str_1)}")
print(f"Первый символ равен {str_1[0]}")
print(f"Последний символ равен {str_1[len(str_1) - 1]}")