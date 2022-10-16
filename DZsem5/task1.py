#   Создайте программу для игры с конфетами человек против человека
#   Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#   Первый ход определяется жеребьёвкой.
#   За один ход можно забрать не более чем 28 конфет.
#   Все конфеты оппонента достаются сделавшему последний ход.
#   Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#   a. Добавьте игру против бота
#   b. Подумайте как наделить бота ''интеллектом''

from math import ceil
from random import randint
import os
os.system('cls')


def checking_input(name):
    n = (
        input(f'\n{name}, введите количество конфет, которое возьмете от 1 до 28: '))
    while not n.isdigit():
        n = (
            input(f'{name}, введите корректное количество конфет: '))
    n = int(n)
    os.system('cls')
    return (n)


def input_dat(name):
    x = checking_input(name)
    while x < 1 or x > 28:
        x = checking_input(name)
    return x


def input_bot(name):
    if counter1 == 0 and value % 29 != 0:
        k = int(value % 29)
    elif counter1 == 0 and value % 29 == 0:
        k = 1
    else:
        k = 29 - includ
    return k


def motion_print(name, k, counter, value):
    print(
        f'Ходил {name}, он взял {k} конфет, теперь у него {counter} конфет. Осталось на столе {value} конфет.')


print('На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
input('\nДля начала игры нажмите "Ввод"')
os.system('cls')
player1 = input('Введите имя первого игрока: ')
player2 = input(
    '\nВведите имя второго игрока, или введите Бот для игры с ботом: ')

if player2 == 'Бот':
    player3 = player2
value = int(input('Введите количество конфет на столе(2021): '))
counter1 = 0
counter2 = 0
counter3 = 0
includ = 0
print('\nКоличество конфет на столе:', value)
flag = randint(0, 2)  # флаг очередности
if flag:
    print(f'Первый ходит {player1}')
elif flag and player2 == 'Бот':
    print(f'Первый ходит {player3}')
else:
    print(f'Первый ходит {player2}')

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        includ = k
        flag = False
        motion_print(player1, k, counter1, value)
    elif player2 == 'Бот':
        k = input_bot(player3)
        counter3 += k
        value -= k
        flag = True
        motion_print(player3, k, counter3, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        motion_print(player2, k, counter2, value)

if flag:
    print(f'Выиграл {player1}')
else:
    print(f'Выиграл {player2}')
    