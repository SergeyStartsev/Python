# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = (input("Введите число : "))
while not n.isdigit():
    n = (input("Введите еще раз: "))
n = int(n)
num = n
i = 2  
new_list = []
while i <= n:
    if n % i == 0:
        new_list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"\nПростые множители числа {num}: {new_list}")