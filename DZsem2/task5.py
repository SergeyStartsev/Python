# Реализуйте алгоритм перемешивания списка


import random
lst = [1, 2, 3, 4, 5,]
print('Начальный список:     ', lst)
for i in range(len(lst)-1, 0, -1):
    j = random.randint(0, i + 1)
    lst[i], lst[j] = lst[j], lst[i]
print('Перемешанный список:  ', lst)