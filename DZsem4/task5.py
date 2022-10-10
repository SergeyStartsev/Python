# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from random import randint
def checking_input(n):
    while not n.isdigit():
        n = (input("Введите еще раз: "))
    n = int(n)
    return (n)

def polinomial(k):
    result = ''
    for i in range(k, 0, -1):
        meaning = '*x^' + str(i)
        result += (str(randint(0, 100)) + meaning + ' + ')
    k = result + str(randint(0, 100)) + '= 0'
    return (k)

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

def calc_poly(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if degree_polynomial(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    deg = 1  
    index = l-1
    while index >= 0:
        if degree_polynomial(st[index]) != -1 and degree_polynomial(st[index]) == deg:
            lst.append(coefficient(st[index]))
            index -= 1
            deg += 1
        else:
            lst.append(0)
            deg += 1

    return lst

def degree_polynomial(k):
    if 'x^' in k:
        i = k.find('^')
        meaning = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        meaning = 1
    else:
        meaning = -1
    return meaning

def coefficient(k):
    if 'x' in k:
        i = k.find('*x')
        num = int(k[:i])
    return num

def create_res(sp):
    new_list = sp[::-1]
    result = ''
    if len(new_list) < 1:
        result = 'x = 0'
    else:
        for i in range(len(new_list)):
            if i != len(new_list) - 1 and new_list[i] != 0 and i != len(new_list) - 2:
                result += f'{new_list[i]}*x^{len(new_list)-i-1}'
                if new_list[i+1] != 0 or new_list[i+2] != 0:
                    result += ' + '
            elif i == len(new_list) - 2 and new_list[i] != 0:
                result += f'{new_list[i]}*x'
                if new_list[i+1] != 0 or new_list[i+2] != 0:
                    result += ' + '
            elif i == len(new_list) - 1 and new_list[i] != 0:
                result += f'{new_list[i]} = 0'
            elif i == len(new_list) - 1 and new_list[i] == 0:
                result += ' = 0'
    return result

k1 = checking_input(
    (input("Введите натуральную степень для первого файла k = ")))
k2 = checking_input(
    (input("Введите натуральную степень для второго файла k = ")))
write_file('task_020_1.txt', polinomial(k1))
write_file('task_020_2.txt', polinomial(k2))

with open('task_020_1.txt', 'r') as data:
    file1 = data.readlines()
with open('task_020_2.txt', 'r') as data:
    file2 = data.readlines()
print(f"Первый многочлен {file1}")
print(f"Второй многочлен {file2}")
lst1 = calc_poly(file1)
lst2 = calc_poly(file2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
write_file("task_020_3.txt", create_res(lst_new))
with open('task_020_3.txt', 'r') as data:
    st3 = data.readlines()
print(f"Результирующий многочлен {st3}")