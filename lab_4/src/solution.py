import matplotlib.pyplot as plt
from copy import deepcopy

from color import set_color, base_color, red, purple

EPS = 0.01

def init_matrix(size):
    matrix = []
    for _ in range(size + 1):
        row = []
        for _ in range(size + 2):
            row.append(0)

        matrix.append(row)

    return matrix
 
def make_slae_matrix(table, n):
    size = len(table)
    matrix = init_matrix(n)

    for i in range(n + 1):
        for j in range(n + 1):

            matrix[i][j] = 0.0
            matrix[i][n + 1] = 0.0

            for k in range(size):
                weight = table[k][2]
                x = table[k][0]
                y = table[k][1]

                matrix[i][j] += weight * pow(x, (i + j))
                matrix[i][n + 1] += weight * y * pow(x, i)

    return matrix
 
def solve_matrix_gauss(matrix):
    size = len(matrix)

    for i in range(size):
        for j in range(i + 1, size):
            if (i == j):
                continue

            k = matrix[j][i] / matrix[i][i]

            for q in range(i, size + 1):
                matrix[j][q] -= k * matrix[i][q]

    result = [0 for i in range(size)]

    for i in range(size - 1, -1, -1):
        for j in range(size - 1, i, -1):
            matrix[i][size] -= result[j] * matrix[i][j]

        result[i] = matrix[i][size] / matrix[i][i]

    return result
 
def find_graph_dots(table, n):
    matrix = make_slae_matrix(table, n)
    result = solve_matrix_gauss(matrix)

    x_arr, y_arr = [], []
    k = table[0][0] - EPS

    size = len(table)
    while (k <= table[size - 1][0] + EPS):
        y = 0
        for j in range(0, n + 1):
            y += result[j] * pow(k, j)

        x_arr.append(k)
        y_arr.append(y)

        k += EPS

    return x_arr, y_arr

def table_changed(table):
    for i in table:
        if i[2] != 1:
            return True
    
    return False

def get_base_table(table):
    base_table = deepcopy(table)
    size = len(base_table)

    for i in range(size):
        base_table[i][2] = 1
    
    return base_table

def plot_graphs(table, n, type_graph, type_dots):
    for i in range(1, n + 1):
        if (i > 2 and i < n):
            continue

        x_arr, y_arr = find_graph_dots(table, i)
        plt.plot(x_arr, y_arr, type_graph, label = "%s\nn = %d" %(type_dots, i))

def solve_task(table):
    try:
        n = int(input("\n%s%sВведите степень аппроксимирующего полинома: %s%s"
            %(set_color, purple, set_color, base_color)))
    except:
        print("\n%s%sОшибка: некорректно введенна степень полинома!%s%s"
            %(set_color, red, set_color, base_color))
        return table

    if table_changed(table):
        base_table = get_base_table(table)
        type_dots = "Diff weights"
        type_graph = "-."

        plot_graphs(base_table, n, "-", "Equal weights")  
    else:
        type_dots = "Equal weights"
        type_graph = "-"

    plot_graphs(table, n, type_graph, type_dots)

    x_arr = [i[0] for i in table]
    y_arr = [i[1] for i in table]

    plt.plot(x_arr, y_arr, 'o', label = "dots")

    plt.legend()
    plt.grid()
    plt.xlabel("Axis X")
    plt.ylabel("Axis Y")
    plt.show()

    return table
