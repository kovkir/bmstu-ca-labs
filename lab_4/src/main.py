from color import set_color, base_color, red, blue
from output import print_menu, print_table
from table import generate_table, change_weight
from solution import solve_task

import matplotlib.pyplot as plt

def main():
    table = generate_table()
    print_table(table)

    action = 1
    while (action != 0):
        print_menu()

        try:
            action = int(input("%s%sВыберете действие: %s%s"
                %(set_color, blue, set_color, base_color)))
        except:
            print("\n%s%sОшибка: ожидался ввод целого числа!%s%s"
                %(set_color, red, set_color, base_color))
            continue
        
        if action == 1:
            print_table(table)
        elif action == 2:
            table = change_weight(table)
        elif action == 3:
            table = solve_task(table)
        elif action > 3:
            print("\n%s%sОшибка: ожидался ввод целого числа от 0 до 3!%s%s"
                %(set_color, red, set_color, base_color))

if __name__ == "__main__":
    main()
