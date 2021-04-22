"""
2. Для удобства хранения, нужно объединить все товары в один объект,
 при этом сохранить структуру типов.
"""

from random import choice, randrange

# Lets imagine this is the continuation of the first task

fruit = ('Apple', 'Pear', 'Cherry', 'Banana', 13)
vegetables = ('Tomato', 'Onion', 'Carrot', 'Cabbage', 17)
berries = ('Blueberry', 'Cranberry', 'Watermelon', 8)

fruit_dict = {v: 'Fruit' for v in fruit if type(v) == str}

veggie_dict = {v: 'Vegetable' for v in vegetables if type(v) == str}

berries_dict = {v: 'Berry' for v in berries if type(v) == str}

fruit_dict.update(veggie_dict)

fruit_dict.update(berries_dict)

print(fruit_dict)