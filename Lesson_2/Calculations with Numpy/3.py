# Задание 3
# Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp.
# Затем поделите a_centered_sp на N-1, где N - число наблюдений.

import numpy as np

a = np.array([[1, 6],
              [2, 8],
              [3, 11],
              [3, 10],
              [1, 7]])

mean_a = np.mean(a, axis=0)

a_centered = a - mean_a

a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1])

div_to_n_m1 = a_centered_sp / (len(a_centered) - 1)
print(div_to_n_m1)
