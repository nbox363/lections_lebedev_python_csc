from types import MethodType


''' descriptor 

Определяет как установить, получить и удалить свойство
'''


class VerySafe:
    ''' Гарантирует, что значение атрибута x будет не отрицательным '''
    def _get_attr(self):
        return self._x

    def _set_attr(self):
        assert x > 0, 'non-negative value required'
        self._x = _x

    def _del_attr(self):
        del self._x

    x = property(_get_attr, _set_attr, _del_attr)


>>> very_safe = VerySafe()
>>> very_safe.x = 42
>>> very_safe.x
# 42
>>> very_safe.x = -42
# AssertionError: non-negative value required
>>> very_safe.y = -42
>>> very_safe.y
# -42


# ###################################################################################


class NonNegative:
    def __get__(self, instance, owner):
        return magically_get_value(...)

    def __set__(self, instance, value):
        assert value >= 0, 'non-negative value required'
        return magically_set_value(...)

    def __delete__(self, instance):
        magically_dellete_value(...)


class VerySafe:
    x = NonNegative()
    y = NonNegative()


>>> very_safe = VerySafe()
>>> very_safe.x = 42
>>> very_safe.x 
# 42
>>> very_safe.x = -42
# AssertionError: non-negative value required
>>> very_safe.y = -42
# AssertionError: non-negative value required


# ###################################################################################


''' __get__

принимает два аргумента 
instance - экземпляр класса или None, 
    если дескриптор был вызван в результате обращения
    к атрибуту класса
    (экземпляр класса, у которого вызывается __get__)
owner - класс, владеющий дескриптором
'''


class Descr:
    def __get__(self, instance, owner):
        print(instance, owner)


class A:
    ''' Владеющий дескриптором Descr '''
    attr = Descr()


>>> A.attr
# None <class '__main__.A'>
>>> A().attr
# <__main__.A object at [...]> <class '__main__.A'>


# ###################################################################################


''' __set__

принимает два аргумента 
instance - экземпляр класса, у которого нужно установить значение атрибута
value - значение атрибута
'''

class Descr:
    def __set__(self, instance, value):
        print(instance, value)


class A:
    attr = Descr()


>>> instance = A()
>>> instance.attr = 42
# <__main__.A object at [...]> 42
>>> A.attr = 42
# 42


# ###################################################################################


''' __delete__

принимает один аргумент -
    экземпляр класса, владующий дескриптором
'''

class Descr:
    def __delete__(self, instance):
        print(instance)


class A:
    attr = Descr()
    

>>> del A().x
# <__main__.A object at [...]>
>>> del A.x


# ###################################################################################


class Descr:
    ''' Дескриптор данных '''
    def __get__(self, instance, owner):
        print('Descr.__get__')

    def __set__(self, instance, value):
        print('Descr.__set__')


class A:
    attr = Descr()


>>> instance = A()
>>> instance.attr
# Descr.__get__
>>> instance.__dict__['attr'] = 42
>>> instance.attr
# Descr.__get__


# ###################################################################################


class Descr:
    ''' Дескриптор с единственным методом __get__ '''
    def __get__(self, instance, owner):
        print('Descr.__get__')


class A:
    attr = Descr()


>>> instance = A()
>>> instance.attr
# Descr.__get__
>>> instance.__dict__['attr'] = 42
>>> instance.attr
# 42


# ###################################################################################


''' Храниение данных в дескрипторах '''


class Proxy:
    ''' Атрибут дескриптора '''
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __set__(self, instance):
        del self.instance


class Something:
    attr = Proxy()


>>> some = Something()
>>> some.attr = 42
>>> other = Something()
>>> other.attr
# 42




class Proxy:
    ''' Словарь '''
    def __init__(self):
        self.data = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if instance not in self.data:
            raise AttributeError
        return self.data['instance']

    def __set__(self, instance, value):
        self.data[instance] = value

    def __delete__(self, instance):
        del self.data[instance]




class Proxy:
    ''' Атрибут экземпляра '''
    def __init__(self, label):
        self.label = label

    def __get__(self, instance, owner):
        # ...
        return instance.__dict__[self.label]

    def __set__(self, instance, value):
        # ...

    def __delete__(self, instance):
        # ...


class Something:
    attr = Proxy('attr')


>>> some = Something()
>>> some.attr = 42
>>> some.attr
# 42


# ###################################################################################


''' Примеры дескрипторов '''


class property:
    def __init__(self, get=None, set=None, delete=None):
        self._get = get
        self._set = set
        self._delete = delete

    def __get__(self, instance, owner):
        if self._get is None:
            raise AttributeError
        return self._get(instance)

    def __set__(self, instance, value):
        # ...

    def __delete__(self, instance):
        # ...


# ###################################################################################


class Something:
    def do_something(self):
        pass


>>> Something.do_something()
# function
>>> Something().do_something()
# bound method


class Function:
    ''' Как работает то, что выше '''
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return MethodType(self, instance, owner)