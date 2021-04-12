from newton_polynom import newton_polynomial 
from spline import spline

def read_file(name_file):
    try:
        with open(name_file, "r") as f:
            table = [list(map(int, string.split())) for string in list(f)]
        return table

    except:
        print("Ошибка чтения файла!\n")
        return []

def read_data(size_table):
    try:
        x = float(input("Введите значение аргумента, для которого выполняется интерполяция: "))
        return 0, x

    except:
        print("Ошибка ввода данных!\n")
        return 1, 0

def print_table(table):
    print("\n{:^5}{:^11}\n".format("x", "y"))

    for i in range(len(table)):
        for j in range(len(table[i])):
            print("%-8.2f" %(table[i][j]), end = '')
        print()

    print()

def main():
    name_file = "../data.txt"

    table = read_file(name_file)
    if (table == []):
        return

    table.sort(key = lambda array: array[0])
    print_table(table)

    r, x = read_data(len(table))
    if (r):
        return

    spl = spline(table, x)
    np = newton_polynomial(table, 3, x)

    print("\nSpline = %.6f" %(spl))
    print("\nNewton_p = %.6f\n" %(np))

if __name__ == "__main__":
    main()
