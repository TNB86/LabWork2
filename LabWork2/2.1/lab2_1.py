import ctypes

import matplotlib.pyplot as plt
import numpy as np


def dll_call(number, lastname=b'Lyubchenko'):
    return lib_dll.TheFunc(lastname, number)


def find():
    x1, x2, x3 = 0, 1, 2
    y1, y2, y3 = dll_call(x1), dll_call(x2), dll_call(x3)
    d1, d2, d3, d4 = np.matrix(f'{x1 * x1} {x1} 1; {x2 * x2} {x2} 1; {x3 * x3} {x3} 1'), \
                     np.matrix(f'{y1} {x1} 1; {y2} {x2} 1; {y3} {x3} 1'), \
                     np.matrix(f'{x1 * x1} {y1} 1; {x2 * x2} {y2} 1; {x3 * x3} {y3} 1'), \
                     np.matrix(f'{x1 * x1} {x1} {y1}; {x2 * x2} {x2} {y2}; {x3 * x3} {x3} {y3}')
    _a = np.linalg.det(d2) / np.linalg.det(d1)
    _b = np.linalg.det(d3) / np.linalg.det(d1)
    _c = np.linalg.det(d4) / np.linalg.det(d1)
    return _a, _b, _c


lib_dll = ctypes.CDLL(r".\Lib2-1.dll")
lib_dll.TheFunc.argtypes = [ctypes.c_char_p, ctypes.c_double]
lib_dll.TheFunc.restype = ctypes.c_double
dots = []

for i in range(11):
    dots.append(dll_call(i))

print(dots)
fig = plt.figure()
fun = plt.plot(dots)
grid = plt.grid(True)
plt.show()
a, b, c = find()
print(a, b, c)
