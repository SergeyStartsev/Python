# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1) ≤ d ≤10^(-10)

from math import pi
from decimal import Decimal
import os
os.system("cls")

d = Decimal(input("Задайте точность для числа Пи: "))
print(f'\nЧисло Пи с заданной точностью {d} равно {str(pi)[:len(str(d))]}')
