from random import random

from color import set_color, base_color, purple, red

SIZE_TABLE = 7
BASE_WEIGHT = 1

def generate_table():
    table = []
    x = random() * 5

    i = 0
    while i < SIZE_TABLE:
        table.append([x + i, random() * 5, BASE_WEIGHT])
        i += 1

    return table

def change_weight(table):
    try:
        index = int(input("\n%s%sВведите номер точки в таблице: %s%s"
            %(set_color, purple, set_color, base_color)))
    except:
        print("\n%s%sОшибка: некорректно введён номер точки!%s%s"
            %(set_color, red, set_color, base_color))
        return table

    if ((index > len(table)) or (index < 1)):
        print("\n%s%sОшибка: в таблице нет точки с таким номером!%s%s"
            %(set_color, red, set_color, base_color))
        return table
        
    try:
        weight =  float(input("\n%s%sВведите новый вес точки: %s%s"
            %(set_color, purple, set_color, base_color)))
    except:
        print("\n%s%sОшибка: некорректно введён вес точки!%s%s"
            %(set_color, red, set_color, base_color))
        return table

    table[index - 1][2] = weight

    return table
