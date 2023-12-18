# Написать функцию triangle, принимающую 1 аргумент — сторону
# равностороннего треугольника, и возвращающую 2 значения
# (с помощью кортежа): периметр и площадь треугольника.

from math import sqrt, pow
def triangle(argument):
  P = 3 * argument
  S = (sqrt(3)/4) * pow(argument, 2)
  return (P, S)
print(triangle(int(input("Enter a side of an equilateral triangle: "))))