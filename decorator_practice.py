import functools
import time
import code
import warnings
import math


def timethis(func=None, *, n_iter=100):
    if func is None:
        return lambda func: timethis(func, n_iter=n_iter)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, end=" ... ")
        acc = float('inf')
        for i in range(n_iter):
            tick = time.perf_counter()
            result = func(*args, **kwargs)
            acc = min(acc, time.perf_counter() - tick)
        print(acc)
        return result
    return inner


result = timethis(sum)(range(10 ** 6))


# ##########################################################################################


def profiled(func):
    """Count how mane times func was called"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        inner.ncalls += 1
        return func(*args, **kwargs)

    inner.ncalls = 0
    return inner


@profiled
def identity(x):
    return x

# print(identity(42)) # 42
# print(identity(42)) # 42
# print(identity.ncalls) # 2


# ##########################################################################################


def once(func):
    """Do something once"""
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if not inner.called:
            func(*args, **kwargs)
            inner.called = True  # already call
    inner.called = False  # don't call else
    return inner


@once
def initialize_setting():
    print("Setting initialized")

# initialize_setting()
# initialize_setting()


# ##########################################################################################


def memoized(func):
    cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return inner


# ##########################################################################################


def deprecated(func):
    code = func.__code__
    warnings.warn_explicit(
        func.__name__ + 'is deprecated',
        category=DeprecationWarning,
        filename=code.co_filename,
        lineno=code.co_firstlineno + 1)
    return func


@deprecated
def identity(x):
    return x


# ##########################################################################################


def pre(cond, massage):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            assert cond(*args, **kwargs), massage
            return func(*args, **kwargs)
        return inner
    return wrapper


@pre(lambda x: r >= 0, 'negative argument')
def checked_log(x):
    return math.log(x)

# checked_log(-42)
