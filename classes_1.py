from collections import deque


class Counter:
    '''I count. That is all'''
    all_counters = []               # атрибут класса

    def __init__(self, initial=0):  # консруктор
        self.value = initial        # запись атрибута
        Counter.all_counters.append(self)

    def increment(self):
        self.value += 1

    def get(self):
        return self.value           # чтение атрибута


c = Counter(42)
c.increment()
c.get()  # 43


# ###################################################################################


class MemorizingDict(dict):
    '''Fixes keys'''
    _history = deque(maxlen=10)

    def set(self, key, value):
        self._history.append(key)
        self[key] = value

    def get_history(self):
        return self._history


d = MemorizingDict({'foo': 42})
d.set('baz', 100500)
d.get_history()  # ['baz']

d = MemorizingDict()
d.set('boo', 500100)
d.get_history()  # ['baz', 'boo']


# ###################################################################################


class Noop:
    '''Fixed set of attributes'''  # No __dict__
    __slots__ = ['some_attribute']


noop = Noop()
noop.some_attribute = 42
noop.some_attribute        # 42
noop.some_other_attribute  # AttrubuteError


# ###################################################################################


class Path:
    def __init__(self, current):
        self.current = current

    def __repr__(self):
        return 'Path({})'.format(self.current)

    @property
    def parent(self):
        return Path(dirname(self.current))


p = Path('./examples/some_file.txt')
p.parent  # Path('./examples/')


# ###################################################################################


class BidDateModel:
    def __init__(self):
        self._params = []

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, new_params):
        assert all(map(lambda p: p > 0, new_params))
        self._params = new_params

    @params.deleter
    def params(self):
        del self._params


model = BidDateModel()
model.params = [0.1, 0.5, 0.4]
model.params  # [0.1, 0.5, 0.4]


# ###################################################################################


class ThreadSafeMixin:
    get_lock = ...

    def increment(self):
        with self.get_lock():
            super().increment()

    def get(self):
        with self.get_lock():
            return super().get()


class ThreadSafeCounter(ThreadSafeMixin, Counter):
    pass


def thread_safe(cls):
    """decorator like class ThreadSafeMixin"""
    orig_increment = cls.increment
    orig_get = cls.get

    def increment(self):
        with self.get_lock():
            orig_increment(self)

    def get(self):
        with self.get_lock():
            return orig_get(self)

    cls.get_lock = ...
    cls.increment = increment
    cls.get = get
    return cls


# ###################################################################################
# ###################################################################################

"""Magic methods"""


class Noop:
    def __getattr__(self, name):  # вызывается, если атрибута нет
        return name


Noop().foo                        # foo


# ###################################################################################


class Guarded:
    guarded = []

    def __setattr__(self, name, value):  # устанавливает значенеи атрибута
        assert name not in self.guarded
        super().__setattr__(name, value)


class Noop(Guarded):
    guarded = ['foobar']

    def __init__(self):
        self.__dict__['foobar'] = 42


# ###################################################################################


class Indentity:
    def __call__(self, x):
        return x


Indentity()(42)
# 42


# ###################################################################################
# ###################################################################################


class A:
    pass


class B(A):
    pass


isinstance(B(), A)  # экземпляр класса
# True
issubclass(B, A)    # класс наследник класса
# True
B.mro()             # порядок разрешения методов
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
