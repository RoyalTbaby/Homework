"""
 Даны два действительных числа. Найти среднее арифметическое и
среднее геометрическое этих чисел
"""
a = 5
b = 16
arithmetic_mean = (a + b) / 2
import math
geometric_mean = (a * b)
result = math.sqrt(geometric_mean)
print(arithmetic_mean)
print(result)