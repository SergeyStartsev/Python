# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр
# Пример:
# 6782 -> 23
# 0,56 -> 11


number = (input("Введите число: ").replace('-', '0').replace('.', '0'))
while not number.isdigit():
    number = (input("Введите еще раз: ").replace('-', '0').replace('.', '0'))

my_sum = sum(map(int, str(number)))
print(f"Сумма цифр числа = {my_sum}")