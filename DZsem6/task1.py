# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

list1 = [i for i in range(1,25) if i%2==0]
li=[]
list(filter((lambda x: li.append((list1[x]))), [x for x in range(1, len(list1), 2)]))
print(list1)
print(sum(li))