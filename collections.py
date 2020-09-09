from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


'''tuple'''
person = ('Bob', 'Carlin', 'May', 12, 1933)
name, birthday = person[:2], person[2:]
# >>> name
# ('Bob', 'Carlin')
# >>> birthday
# ('May', 12, 1933)

NAME, BIRTHDAY = slice(2), slice(2, None)
person[NAME]  # ('Bob', 'Carlin')
person[BIRTHDAY]  # ('May', 12, 1933)


'''namedtuple'''
Person = namedtuple('Person', ['name', 'age'])
p = Person('Bob', 77)

p._fields  # ('name', 'age')
p.name, p.age  # Bob 77
p._asdict()  # OrderedDict([('name', 'Bob'), ('age', 77)])
p._replace(name='Bill')  # Person(name='Bill', age=77)


'''list'''
[[0] for i in range(2)]  # одномерный массив
# [[0], [0]]
print([([0] * 3) for i in range(5)])  # двумерный массив
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]

q = deque()
q = deque([1, 2, 3])
q.appendleft(0)
q.popleft()

#####################################################################

xs, ys, zs = {1, 2}, {2, 3}, {3, 4}
set.union(xs, ys, zs)  # xs | ys | zs
set.intersection(xs, ys, zs)  # xs & ys & zs
set.difference(xs, ys, zs)  # xs - ys - zs

#####################################################################

d = dict(foo='bar')
d_1 = dict(d, boo='baz')  # копирование словаря
d_2 = dict.fromkeys(['foo', 'bar'], 0)  # {'foo': 0, 'bar': 0}
d_3 = dict.fromkeys('abcd', 0)  # {'a': 0, 'b': 0, 'c': 0, 'd': 0}
d_4 = {ch: [] for ch in 'abcd'}  # {'a': [], 'b': [], 'c': [], 'd': []}

g = defaultdict(set, **{'a': {'b'}, 'b': {'c'}})
g['c'].add('a')  # {'a': {'b'}, 'b': {'c'}, 'c': {'a'}}

o = OrderedDict([('foo', 'bar'), ('boo', 42)])

c = Counter(['foo', 'foo', 'foo', 'bar'])  # Counter({'foo': 3, 'bar': 1})
c['foo'] += 1  # ({'foo': 4, 'bar': 1})

c. most_common(1)  # [('foo', 4)]

c.subtract({'foo': 2})  # Counter({'foo': 2, 'bar': 1})
