from numpy.polynomial.legendre import leggauss
from numpy import arange
import matplotlib.pyplot as plt
from math import pi, cos, sin, exp

from color import set_color, base_color, red, blue, green, purple, yellow

def gauss_method(func, a, b, n):
    args, coefs = leggauss(n)
    res = 0

    for i in range(n):
        res += (b - a) / 2 * coefs[i] * func((b + a) / 2 + (b - a) * args[i] / 2)

    return res

def simpson_method(func, a, b, n):
    h = (b - a) / (n - 1)
    x = a
    res = 0

    for i in range((n - 1) // 2):
        res += func(x) + 4 * func(x + h) + func(x + 2 * h)
        x += 2 * h

    return res * (h / 3)

def function(tao):
    coef = lambda x, y: 2 * cos(x) / (1 - (sin(x) ** 2) * (cos(y) ** 2))
    f = lambda x, y: (4 / pi) * (1 - exp(-tao * coef(x, y))) * cos(x) * sin(x)

    return f

def integrate(func, limits, nodes, methods):
    internal = lambda x: methods[1](lambda y: func(x, y), limits[1][0], limits[1][1], nodes[1])
    res =  methods[0](internal, limits[0][0], limits[0][1], nodes[0])

    return res

def graph(func, borders, label):
    x = []
    y = []

    for tau in arange(borders[0], borders[1] + borders[2], borders[2]):
        x.append(tau)
        y.append(func(tau))

    plt.plot(x, y, label = label)

def choose_action():
    try:
        action = int(input("%s%sПродолжть добавление графиков?\n    1 - Да\n    0 - нет\n%s%s"
            %(set_color, green, set_color, base_color)))

        if action != 1 and action != 0:
            print("\n%s%sОшибка: неверно введено число!%s%s" 
                %(set_color, red, set_color, base_color))
        
            action = choose_action()
            
    except:
        print("\n%s%sОшибка: неверно введено число!%s%s" 
            %(set_color, red, set_color, base_color))

        action = choose_action()

    return action

def input_tau():
    try:
        tau = float(input("\n%s%sВведимте τ: %s%s"
            %(set_color, blue, set_color, base_color)))
    except:
        print("\n%s%sОшибка: неверно введено число!%s%s" 
            %(set_color, red, set_color, base_color))

        return 0, 1

    return tau, 0

def choose_method(str):
    try:
        method = int(input("%s%sМетод для %s интегрирования: %s%s" 
            %(set_color, yellow, str, set_color, base_color)))

        if (method != 1 and method != 2):
            print("\n%s%sОшибка: неверно выбран метод!%s%s"
                %(set_color, red, set_color, base_color))
            return -1, -1

        n = int(input("%s%sКол-во узлов для %s интегрирования: %s%s" 
            %(set_color, yellow, str, set_color, base_color)))

        if (n < 1):
            print("\n%s%sОшибка: количество узлов должно быть больше нуля!%s%s"
                %(set_color, red, set_color, base_color))
            return -3, -3
        
        if (method == 2 and n < 3):
            print("\n%s%sОшибка: количество узлов для метода Симпсона должно быть больше 2!%s%s"
                %(set_color, red, set_color, base_color))
            return -4, -4

        print()

    except:
        print("\n%s%sОшибка: неверно выбран метод!%s%s"
            %(set_color, red, set_color, base_color))
        return -1, -1

    return gauss_method if method == 1 else simpson_method, n

def main():    
    tau, err = input_tau()
    if err:
        return

    while True:

        print("\n%s%sВыбор метода интегрирования:\n    1 - Гаусс\n    2 - Симпсон\n%s%s"
            %(set_color, purple, set_color, base_color))
        
        external_method, n = choose_method("внешнего")
        if n < 0:
            return

        internal_method, m = choose_method("внутреннего")
        if m < 0:
            return

        integ_param = lambda t: integrate(function(t), [[0, pi / 2], [0, pi / 2]], 
            [n, m], [external_method, internal_method])

        print("%s%sРезультат интегрирования при τ = %.2f: %s%s%.4f"
            %(set_color, blue, tau, set_color, base_color, integ_param(tau)), "\n")

        label = "n = " + str(n) + ", m = " + str(m) + ";  "
        label += "Simpson " if external_method == simpson_method else "Gauss "
        label += "- Simpson" if internal_method == simpson_method else "- Gauss"

        graph(integ_param, [0.05, 10, 0.05], label)

        if choose_action() == 0:
            break

    plt.legend()
    plt.ylabel("Result")
    plt.xlabel("Tau value")
    plt.show()

if __name__ == "__main__":
    main()
