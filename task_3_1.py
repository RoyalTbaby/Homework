"""
1. На склад поступил новый товар.
Надо пересмотреть склад и исправить ошибки, сделать первую букву заглавной.
Так же сделать все типы товаров должны быть неизменяемыми,
чтобы кто-то случайно не перепутал их снова.
В овощи забыли добавить капусту. (Цифра в категории - это цена товара этого типа.)
"""

from random import choice, randrange

fruit = ('apple', 'pear', 'cherry', 'banana', 13)
vegetables = ['tomato', 'onion', 'carrot', 17]
berries = ('blueberry', 'cranberry', 'watermelon', 8)

new_fruit_list = []
for elem in fruit:
    if type(elem) == str:
        new_fruit_list.append(elem.capitalize())
else:
    new_fruit_list.append(elem)

fruit = tuple(new_fruit_list)

new_berries_list = []
for elem in berries:
    if type(elem) == str:
        new_berries_list.append(elem.capitalize())
else:
    new_berries_list.append(elem)

berries = tuple(new_berries_list)

vegetables.insert(3, 'cabbage')

new_veggie_list = []
for elem in vegetables:
    if type(elem) == str:
        new_veggie_list.append(elem.capitalize())
else:
    new_veggie_list.append(elem)

vegetables = tuple(new_veggie_list)

print(fruit)
print(vegetables)
print(berries)