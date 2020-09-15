from sys import path


''' Модуль - хранилище имен

В момент запуска name = __main__
В момент импорта имени файла
У модуля есть атрибуты
__name__, __file__, __doc__, __cached__
'''

if name == '__main__':
    pass


>>> import matplotlip as mtp

>>> sys.path      # чтобы импортировать модуль, он должен быть в sys.path

>>> __all__ = []  # то, что импортируется при import *


# ###################################################################################
# ###################################################################################


''' Packeges


useful.py
    __init__.py
    bar.py
    foo.py
'''


>>> from . import useful  # относительный импорт

'''
useful.py
    __init__.py
    bar.py
        __init__.py
        boo.py
    foo.py
'''

# находясь в пакете bar
>>> from . import smt
>>> from ..foo import smt_else


'''
задача __init__.py инициализировать пакет
там можно объявить глобальные переменные для пакета
оградить пакет фасадом
'''


'''Фасад'''

# useful/bar/__init__.py
from .boo import *

__all__ = boo.__all__

#useful/__init__.py
from .boo import *
from .bar import *

__all__ = foo.__all__ + bar.__all__


'''Исполняемые модули и пакеты'''

# useful/__main__.py
print('It works')

# useful/__init__.py
print('useful/__init__.py')


$ python -m useful
useful.__init__.py
It works

$ python -m useful.__main__
useful.__init__.py
It works


# ###################################################################################
# ###################################################################################


'''Система импорта'''


def import_wrapper(name, *args, imp=__import__):
    print('importing ', name)
    return imp(name, *args)


>>> import builtins
>>> builtins.__import__ = import_wrapper
>>> import collections
# importing collections
# importing _collections_abc
# importing _collections
# import operator
# ...


'''Циклические импорты'''

'''
useful.py
    __init__.py
    bar.py
        __init__.py
        boo.py
    foo.py
'''

# useful/__init__.py
from .foo import *

some_variable = 42


# useful/foo.py
from . import some_variable

def foo():
    print(some_variable)


>>> import useful
# ImportError: cannot import name 'some_variable'


'''Три способа для борьбы с циклическими импортами'''

# 1 вынести функциональность
# useful/_common.py
some_variable = 42


# 2 локальный импорт
# useful/foo.py
def foo():
    from . import some_variable
    print(some_variable)


# 3 импорт в конце модуля
# useful/__init__.py
some_variable = 42

from .foo import *