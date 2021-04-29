# У нас есть кафе. Нам нужно написать программу для работы баристы.
# Перед тем как писать программу, надо создать тестовые данные.

# 1. Каждый день в кафе заходит от 5 до 20 покупателей. Каждый покупатель берёт от 1 до 3 чашек кофе.
# Нужно написать функцию, которая будет генерировать тестовые данные при каждом вызове.
# 2. К каждой покупке нужно добавить дату и время до минуты (2 отдельные переменные).
# Время работы кафе - с 9 до 20 часов.
# 3. Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.

import random
import datetime

def daily_check():
    number_of_clients = random.randrange(5, 21)
    for i in range(1, number_of_clients):
        order_purchase = random.randrange(1, 4)
        daily_sum = 0
        for e in range(order_purchase):
            coffee_order = random.randrange(2, 6)
            daily_sum = daily_sum + coffee_order
        print(f' Customer {i}, The number of orders {order_purchase}, Receipt  {daily_sum }')

print(daily_check())

from datetime import date, time, datetime, timedelta
from random import randint

d = date.today() + timedelta(days=randint(1, 5))
t = time(9, 0, 0)
dt = datetime.combine(d, t) + timedelta(seconds=randint(1, 41000))

print(dt)