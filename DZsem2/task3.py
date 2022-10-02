# Задайте список из n чисел последовательности (1+ 1/n)^n 
# выведите на экран их сумму
# (округляйте до 3 знаков после запятой).

n = int(input('Введите число: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 3) for x in range (1, n + 1)]   
        
print(sequence(n))

print(round(sum(sequence(n))))