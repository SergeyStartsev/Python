# Напишите программу, которая будет преобразовывать десятичное число в двоичное
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


n = (input("Введите число: "))
while not n.isdigit():
    n = (input("Введите еще раз: "))
n1 = int(n)  
s = ""
while n1 != 0:
    s += str(n1 % 2)
    n1 //= 2
print(f'\nДесятичное число {n} в виде двоичного числа: {s}\n')