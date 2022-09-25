# print('hello world')

# Типы данных справедливы
# int, float, boolean, str, list None и др.

# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(a)
# print(type(a))
# print(b)
# print(type(b))
# value = 12334
# print(value)
# print(type(value))
# s = 'Привет мир'
# print(s)
# print(type(s))
# s = "Привет 'мир'"
# print(s)
# s = 'Привет "мир"'  # или кавычки наоборот
# print(s)
# s = '\nПривет \'мир'
# print(s)

# # Интерполяция (числа и строки)
# a = 123
# b = 1.23
# s = 'Привет мир'
# # Способы вывода
# print(a, b, s)
# print(a, ' - ', b, ' - ', s)
# print('{} - {} - {}'.format(a, b, s))  # Формат
# print('{1} - {2} - {0}'.format(a, b, s))  # Порядок вывода можно менять
# print(f'{a} - {b} - {s}')  # Интерполяция вывода

# # Логическая переменная
# ft = True
# print(ft)
# ff = False
# print(ff)

# # Списки (массив)
# list = []  # пустой лист
# print(list)
# list = [1, 2, 3]  # лист значений
# print(list)
# list = ['1', '2', '3', 'hello']  # лист строк
# print(list)
# # можно миксовать и значения и строки и логику(но лучше хранить значения одного типа)
# list = ['1', '2', '3', 'hello', 1, 2, 3, True]
# print(list)

# # пробел может все сломать
# list = ['1', '2', '3']
# col = ['hello', 1, 2, 3, True]
# print(list)
# print(col)

# # Ввод и вывод данных
# # print() – отвечает за вывод данных
# # input() – отвечает за ввод данных
# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите а')  # Введите а = 10
# a = input()
# print('Введите b')  # Введите b = 20
# b = input()
# print(a, '+', b, '=', a+b)  # строка ответ  = 10 + 20 = 1020

# print('Введите а')  # Введите а = 12
# a = int(input())  # если теребуется челое число то функция"int" говорит мы хотим его
# print('Введите b')  # Введите b = 23
# b = int(input())
# print(a, '+', b, '=', a+b)  # вывод 12 + 23 = 35

# print('Введите а')  # Введите а = 1.2
# # если теребуется вещественное челое число то функция"float" говорит мы хотим его
# a = float(input())
# print('Введите b')  # Введите b = 3.4
# b = float(input())
# print(a, '+', b, '=', a+b)  # вывод 1.2 + 3.4 = 4.6

# Арифметические операции
# +, -,*, /, %, //,**
# Приоритет операций
# **, ⊕, ⊖,*, /, //, %, +, -
# ( ) Скобки меняют приоритет
# a = 123
# b = -321  # Унарный минус(-), есть и плюс(+) но практически не используется
# c = a+b
# print(c)

# a = 12
# b = 8
# c = a//b  # (//) деление в целых числах
# print(c)

# a = 12
# b = 8
# c = a//b  # (//) деление в целых числах
# print(c)

# a = 12
# b = 8
# c = a % b  # (%) остаток от деления
# print(c)

# a = 2
# b = 8
# c = a ** b  # (**) возведение в степень
# print(c)

# a = 1.3
# b = 3
# c = a * b  # вывод 3.9000000000000004 , особенность хранения вещественных чисел
# print(c)

# a = 1.3
# b = 3
# # (round) без аргумента округляет по мат правилам, можно указать кол-во знаков вывода
# c = round(a * b, 3)
# print(c)

# a = 3
# #a = a+5
# a += 5
# print(a)

# a, b, c = 1, 2, 3
# # a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))


# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |,^
# Кое-что ещё: is, is not, in, not in

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 != 2
# print(a)

# a = 1 == 2
# print(a)

# a = 'Приветики'
# b = 'Приветики'
# print(a == b)

# a = 1 < 3 < 5  # тройное  неравенство и 4 тоже работает
# print(a)

# fanc = 1
# T = 4
# x = 2
# print(fanc < T > (x))  # тоже тройное неравенство, можно "x" без скобок

# Логическая операция
# f = 1 > 2 or 4 < 6  # "or" или
# print(f)

# f = [1, 2, 3, 4]
# # print(f)
# # print(2 in f)  # (2 in f) содержиться ли "2" в этом списке
# # print(not 2 in f)  # (not 2 in f) отрицание

# is_odd = f[0] % 2 == 0  # является ли четным?
# print(is_odd)
# # более верная запись в pyton
# is_odd = not f[0] % 2
# print(is_odd)

# Управляющие конструкции: if, if-else
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# # Логический оператор - elif
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# Циклы
# Управляющие конструкции: while
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции: while-else
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции: for
# for i in 1, 2, 3, 4, 5: # можно сразу так
#     print(i**2)

# list = [1, 2, 3, 4, 10, 5]
# for i in list:
#     print(i)

# r = range(10) # range - это объект
# for i in range(5):  # можно сразу так, без создания переменной 'r'
#     print(i)

# for i in range(1, 5):  # можно указать нужный диапазон'
#     print(i)

# for i in range(1, 10, 2):  # третий аргумент приращение (шаг)
#     print(i)

# for i in 'qwe - rty':  # тоже и со строкой, с точностью до пробелов и знаков
#     print(i)

# # Вложенные циклы
# line = ""
# for i in range(4):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# Немного о строках
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))  # 39
# print('ещё' in text)  # True
# print(text.isdigit())  # False
# print(text.islower())  # True
# print(text.replace('ещё', 'ЕЩЁ'))
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])  # c
# print(text[1])  # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])  # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2]

# Списки: введение
## list = list
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)  # red green blue
# for e in colors:
#     print(e*2)  # redred greengreen blueblue
# colors.append('gray')  # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])  # True
# colors.remove('red')  # del colors[0] # удалить элемент

# Функции: Это фрагмент программы, используемый многократно

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return


# arg = 2
# print(f(arg))
# print(type(f(arg)))