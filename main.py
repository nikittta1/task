import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 2*x**2 + 16/x


def secant_method(f, x0, x1, tol, max_iter):
    iter_count = 0
    x_values = []
    f_values = []

    while iter_count < max_iter:
        df = (f(x1) - f(x0)) / (x1 - x0)

        x2 = x1 - f(x1) / df

        print(f"Итерация {iter_count + 1}: x = {x2}")

        x_values.append(x2)
        f_values.append(f(x2))
        if abs(x2 - x1) < tol:
            if abs(df) < tol:
                return x2, f(x2), x_values, f_values
            else:
                return x2, f(x2), x_values, f_values, "Не оптимально"

        x0 = x1
        x1 = x2
        iter_count += 1

    return None, None, x_values, f_values, "Не сошелся"


x0 = -1
x1 = 5
tolerance = 1e-6
max_iterations = 100

result, f_result, x_values, f_values, status = secant_method(f, x0, x1, tolerance, max_iterations)


if result is not None:
    x_extremum = result
    print(f"Экстремум функции: x = {x_extremum}")
else:
    print(f"Метод секущих завершился с сообщением: {status}")

x = np.linspace(min(x_values) - 1, max(x_values) + 1, 100)
plt.plot(x, f(x), label='f(x)')
plt.scatter(x_values, f_values, color='red', marker='o', label='Итерации')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()