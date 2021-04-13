from color import set_color, base_color, green, yellow

def print_table(table):
    print("\n\t%s%sСгенерированная таблица\n\n" %(set_color, yellow) +
          "  №    |     X     |     Y    |    W \n" + 40 * "-")

    size = len(table)

    for i in range(size):
        print("  %-3d  |   %-5.2f   |   %-4.2f   |   %-5.2f   " 
            %(i + 1, table[i][0], table[i][1], table[i][2]))

def print_menu():
    print("%s%s\
        \n1. Распечатать таблицу\
        \n2. Изменить вес точки\
        \n3. Вывести результаты\
        \n0. Выйти%s%s\n"
        %(set_color, green, set_color, base_color))
        