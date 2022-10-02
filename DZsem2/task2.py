# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = (input("Введите число N: "))
while not n.isdigit():
    n = (input("Введите еще раз: "))
n = int(n)
solving = [1]
for i in range(2, n + 1):
    solving.append(solving[i - 2] * i)
print(solving)