""" Decorator it's just function which return other function
    Декоратор - способ модифицировать поведение функции, сохраняя читаемость кода
    Декораторы бывает без аргументов: @trace
               с аргументами @trace(sys.stderr)
               с опциональными аргументами
"""

import functools
import sys

# #############################################


@trace
def foo(x):
    return 42
# ==


def foo(x):
    return 42


foo = trace(foo)

# #############################################


def trace(func):
    """Печатает имя функции и аргументы с которыми она была вызвана"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    # # inner.__module__ = func.__module__
    # # inner.__name__ = func.__name__
    # # inner.__doc__ = func.__doc__
    # functools.update_wrapper(inner, func)
    return inner


@trace  # identity = trace(identity)
def identity(x):
    """ I do nothing usful"""
    return x


# Если убрать декоратор (@trace), то мы увидем 'identity  I do nothing usful'
# Если декоратор будет - 'inner None'
print(identity.__name__, identity.__doc__)

identity(42)

# #############################################

# deco = trace(sys.stderr)
# identity = deco(identity)
@trace(sys.stderr)
def identity(x):
    """ I do nothing usful"""
    return x

# #############################################


def trace(handle):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            print(func.__name__, args, kwargs,
                  file=handle)
            return func(*args, **kwargs)
        return inner
    return decorator


def trace(func=None, *, handle=sys.stdout):
    """Same deco 'trace', take argument, and can call without arguments"""
    if func is None:
        return lambda func: trace(func, handle=handle)  # deco

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return inner

# #############################################


def with_arguments(deco):  # декоратор для декоратора, принимает декоратор
    @functools.wraps(func)
    def wrapper(*dargs, **dkwargs):  # декоратор deco
        def decorator(func):
            # применяем декоратор к функции
            result = deco(func, *dargs, *dkwargs)
            functools.update_wrapper(result, func)
            return result
        return decorator
    return wrapper

# 1) with_arguments принимает декоратор deco
# 2) заворачивает его во wrapper, так как deco - декоратор
#    c аргуементами
# 3) decorator конструирует новый декоратор с помощью deco
#    и копирует в него внутренние атрибуты функции func


@with_arguments
def trace(func, handle):
    """How it's work"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs, file=handle)
        return func(*args, **kwargs)
    return inner


@trace(sys.stderr)
def identity(x):
    return x


# #############################################
# #############################################

def my_print(func):
    def zz():
        return func()
    return zz


@my_print
def z():
    return 42


z()

# ##########################################

cache = {}


def remember(func):
    def inner(arg):
        if arg not in cache:
            cache[arg] = func(arg)
        return cache[arg]
    return inner


@remember
def square(x):
    return x * x
