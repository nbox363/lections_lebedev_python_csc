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

>>> 