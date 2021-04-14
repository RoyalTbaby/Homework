"""
Даны катеты прямоугольного треугольника. Найти его гипотенузу и
площадь.
"""

leg_a = 3
leg_b = 4
hypotenuse = ((leg_a ** 2) + (leg_b ** 2)) ** 0.5
print(hypotenuse)

square = (leg_a * leg_b) / 2
print(square)
