import ctypes
import matplotlib.pyplot as plt
import os


def load_lib(_item):
    return ctypes.CDLL(os.path.join(root, _item))


def is_lib_loaded(_item):
    try:
        ctypes.CDLL(os.path.join(root, _item))
    except OSError:
        print(f"Library {_item} can't be loaded")
        return False
    else:
        print(f"Library {_item} successfully loaded")
        return True


def UC(_libs, _con_libs):
    print("Enter function")
    for i, item in enumerate(_libs):
        print(f"\t{i + 1}){item};")
    print("\t0)Exit")
    while True:
        chose = int(input())
        if chose in range(1, len(_libs)+1):
            data_graph(_con_libs[chose-1])
        elif chose == 0:
            break
        else:
            print("Push button from list")


def data_graph(_item):
    try:
        func_name = _item.FuncName
        the_func = _item.TheFunc
    except AttributeError:
        print("Function damaged")
        return
    func_name.restype = ctypes.c_char_p
    the_func.argtype = ctypes.c_double
    the_func.restype = ctypes.c_double
    name = func_name().decode('ascii')
    x, y = [], []
    for i in range(11):
        x.append(i)
        y.append(the_func(ctypes.c_double(i)))
    make_graph(x, y, name)


def make_graph(x, y, marker):
    plt.figure(figsize=(15, 8))
    plt.plot(x, y)
    plt.xticks(x)
    plt.yticks(y)
    plt.title(marker)
    plt.show()


root = r'..\Dlls\Plugins'
dlls = ['Lib.dll',
        'Lib2-2-1.dll',
        'Lib2-2-2.dll',
        'Lib2-2-3.dll',
        'Lib2-2-3-1.dll',
        'Lib2-2-3-2.dll'
        ]

libs = list(filter(is_lib_loaded, dlls))
con_libs = list(map(load_lib, libs))
UC(libs, con_libs)
