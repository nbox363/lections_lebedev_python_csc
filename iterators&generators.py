from itertools import islice
from itertools import count, cycle, repeat
from itertools import tee
from functools import wraps
import os
from contextlib contextmanager


''' Iterators 

Метод __iter__ возвращает от объекта итератор
Метод __next__ возврващет следующих элемент
'''
# ###################################################################################


'''Как работает'''
for x in xs:
    do_smt(x)

it = iter(xs)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    do_smt()


# ###################################################################################


''' Операторы in и not in используют метод __contains__'''


class object:
    '''Реализация __contains__ по умолчанию'''
    # ...

    def __contains__(self, target):
        for item in self:
            if item == target:
                return True
        return False


# ###################################################################################


class Identity:
    ''' Если объект перегружает __getitem__ 
    то он становится итератором '''

    def __getitem__(self, idx):
        if idx > 5:
            raise IndexError(idx)
        return idx


list(Identity())  # [0, 1, 2, 3, 4, 5]


# ###################################################################################


class Seq_iter:
    def __init__(self, instance):
        self.instance = instance
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            res = self.instance[self.idx]
        except IndexError:
            raise StopIteration

        self.idx += 1
        return res


# ###################################################################################


class object:
    '''Реализация __iter__'''
    # ...

    def __iter__(self):
        if not hasattr(self, '__getitem__'):
            cls = self.__class__
            msg = '{} object is not iterable'
            raise TypeError(msg.format(cls.__name__))
        return Seq_iter(self)


# ###################################################################################
# ###################################################################################


''' Generators 

Генератор останавливает свое выполнение в точки yield
'''


def g():
    print('Started')
    x = 42
    yield x
    x = + 1
    yield x
    print('Done')

>>> type(g)
# class 'function'
>>> gen = g()
# class 'generator'
>>> next(gen)
# Started
# 42
>>> next(gen)
# 43
>>> next(gen)
# Done
# StopIteration


# ###################################################################################


def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


# ###################################################################################


def map(func, iterable, *rest):
    for args in zip(iterable, *rest):
        yield func(*args)


# ###################################################################################


def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item


# ###################################################################################


def count(start=0):
    while True:
        yield start
        start += 1


# ###################################################################################


def enumerate_(iterable, start=0):
    return zip(count(start), iterable)


# ###################################################################################


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left, self.right = left, right

    def __iter__(self):
        for node in self.left:
            yield node.value
        yield self.value
        for node in self.right:
            yield node.value


# ###################################################################################


gen = (x ** 2 for x in range(10**42) if x % 2 == 1)  # generator object


# ###################################################################################


def g():
    res = yield
    print(f"Got {res}")
    res = yield 42
    print(f"Got {res}")

>>> gen = g()
>>> next(gen)
>>> next(gen)
# Got 'None'
# 42
>>> next(gen)
# Got 'None'
# StopIteration


# ###################################################################################


def g():
    try:
        yield 42
    finally:
        print('Done')


>>> gen = g()
>>> next(gen)
# 42
>>> gen.close()  # throw GeneratorExit
# Done


# ###################################################################################


def grep(pattern):
    print("Loking for {!r}".format(pattern))
    while True:
        line = yield
        if pattern in line:
            print(line)


>>> gen = grep("Gotcha!")
>>> next(gen)
# Loking for 'Gotcha!'
>>> gen.send("This line doesn't have waht we're looking for")
>>> gen.send("This one does. Gotcha!")
# This one does. Gotcha!


# ###################################################################################


def coroutine(g):
    '''Декоратор, скрывающий вызов next(gen)'''
    @functools.wraps(g)
    def inner(*args, **kwargs):
        gen = g(*args, **kwargs)
        next(gen)
        return gen
    return inner 


# ###################################################################################


class cd:
    '''Change current work dir'''
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.saved_cwd = os.getcwd()
        os.chdir(self.path)

    def __exit(self, *exc_info):
        os.chdir(self.saved_cwd)


@contextmanager             # позволяет записать менеджера контекста в виде генератора
def cd(path):               # __init__
    '''like cd before'''
    old_path = os.getcwd()  # __enter__
    os.chdir(path)
    try:
        yield               # --------
    finally:
        os.chdir(old_path)  # __exit__


# ###################################################################################
# ###################################################################################


''' Itertools '''


'''islice

позволяет делать слайсы произволных объектов
с поддержкой иттерации
'''

xs = range(10)
list(islice(xs, 3))        # xs[:3]
# [1, 2, 3]
list(islice(xs, 3, None))  # xs[3:]
# [3, 4, 5, 6, 7, 8, 9]
list(islice(xs, 3, 8, 2))  # xs[3:8:2]
# [3, 5, 7]


# ###################################################################################


''' count, cycle, repeat '''


def take(iterable, n):
    return list(islice(iterable, n))

>>> list(take(range(10), 3)
# [0, 1, 2]


>>> take(3, count(0, 5))
# [0, 5, 10]
>>> take(3, cycle([1, 2, 3]))  # перечисляет элементы переданного iterable
# [1, 2, 3]
>>> take(3, repeat(42, 2))     # повторяет элемент
# [42, 42]


# ###################################################################################


''' tee

позволяет дупблировать итератор
'''


it = range(3)
a, b, c = tee(it, 3)  # принимает иетератор и сколько раз нужно размножить
>>> list(a), list(b), list(c)
# ([0, 1, 2], [0, 1, 2], [0, 1, 2])


it = iter(range(3))
a, b = tee(it, 2)
used = list(it)
>>> list(a), list(b)
# ([], [])
