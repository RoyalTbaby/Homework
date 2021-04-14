"""
2. Даны действительные числа x и y. Получить 1+ |xy|
"""
import math
x = -6
x = math.fabs(x)

y = 3
y = math.fabs(y)

result = (x - y) / (1 + (x * y))
print(result)