import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

EPS = 1e-6

def read_file(name_file):
    try:
        with open(name_file, "r") as f:
            table = [list(map(float, string.split())) for string in list(f)]
        return table

    except:
        print("Ошибка чтения файла!")
        return []

def read_data(size_table):
    try:
        nx = int(input("Введите степень аппроксимирующего полинома - nx: "))

        if (nx <= 0):
            print("nx должна быть > 0!")
            return 1, 0, 0, 0, 0
        elif (nx >= size_table):
            print("Слишком большая степень аппроксимирующего полинома nx для данной таблицы!")
            return 2, 0, 0, 0, 0

        ny = int(input("Введите степень аппроксимирующего полинома - ny: "))

        if (ny <= 0):
            print("ny должна быть > 0!")
            return 3, 0, 0, 0, 0
        elif (ny >= size_table):
            print("Слишком большая степень аппроксимирующего полинома ny для данной таблицы!")
            return 4, 0, 0, 0, 0

        x = float(input("\nВведите x, для которого выполняется интерполяция: "))
        y = float(input("Введите y, для которого выполняется интерполяция: "))

        return 0, nx, ny, x, y

    except:
        print("Ошибка ввода данных!")
        return 5, 0, 0, 0, 0

def print_table(table):
    print("\n\t\tz[x, y]\n")

    for i in range(len(table)):
        for j in range(len(table[i])):
            print("%-9.2f" %(table[i][j]), end = '')
        print()

    print()

def search_index(table, x, n):
    index = 0

    for i in table:
        if (i[0] > x):
            break
        index += 1

    if index >= len(table) - n:
        return len(table) - n - 1

    l_border = index
    r_border = index

    while (n > 0):
        if (r_border - index == index - l_border):
            if (l_border > 0):
                l_border -= 1
            else:
                r_border += 1
        else:
            if (r_border < len(table) - 1):
                r_border += 1
            else:
                l_border -= 1
        n -= 1

    return l_border

def divided_difference(x0, y0, x1, y1):
    if (abs(x0 - x1) > EPS):
        return (y0 - y1) / (x0 - x1)

def newton_polynomial(table, n, x):
    index = search_index(table, x, n)
    np = table[index][1]

    for i in range(n):
        for j in range(n - i):
            table[index + j][1] = divided_difference(
                table[index + j][0],         table[index + j][1],
                table[index + j + i + 1][0], table[index + j + 1][1])

        mult = 1
        for j in range(i + 1):
            mult *= (x - table[index + j][0])

        mult *= table[index][1]
        np += mult
        
    return np

def multivariate_interpolation(table, nx, ny, x, y):
    res_array = []

    for i in range(len(table)):
        array = []
        for j in range(len(table)):
            array.append([j, table[i][j]])

        res_array.append(newton_polynomial(array, nx, x))

    array = []
    for i in range(len(table)):
        array.append([i, res_array[i]])

    return newton_polynomial(array, ny, y)

def picture_3D(table, x, y, np):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')

    x_list = []
    y_list = []
    z_list = []
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            x_list.append(i)
            y_list.append(j)
            z_list.append(table[i][j])

    Axes3D.scatter(ax, x_list, y_list, z_list, zdir = "z", s = 20, c = "red", depthshade = True)
    Axes3D.scatter(ax, x, y, np, zdir = "z", s = 20, c = "blue", depthshade = True)
    plt.show()

def main():
    name_file = "./data.txt"

    table = read_file(name_file)
    if (table == []):
        return

    print_table(table)
    r, nx, ny, x, y = read_data(len(table))

    if (r):
        return

    np = multivariate_interpolation(table, nx, ny, x, y)

    print("\nРезультат интерполяции z(x,y) = %.2f\n" %(np))
    picture_3D(table, x, y, np)

if __name__ == "__main__":
    main()
