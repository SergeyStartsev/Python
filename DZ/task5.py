# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
#  A(3, 6) B(2, 1) -> 5, 09
#  A(7, -5) B(1, -1) -> 7, 21

first_point = list(map(int, input(
    "Введите координаты точки 1 (x y): ").split()))
second_point = list(map(int, input(
    "\nВведите координаты точки 2 (x y): ").split()))
distance = (((second_point[0] - first_point[0])**2 +
            (second_point[1] - first_point[1])**2) ** (0.5))
print(
    f"\nРасстояние между двумя точками в 2D пространстве равно {round(distance, 2)}\n")