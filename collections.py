from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


''' tuple '''
person = ('Bob', 'Carlin', 'May', 12, 1933)
name, birthday = person[:2], person[2:]
# >>> name
# ('Bob', 'Carlin')
# >>> birthday
# ('May', 12, 1933)

NAME, BIRTHDAY = slice(2), slice(2, None)
person[NAME]      # ('Bob', 'Carlin')
person[BIRTHDAY]  # ('May', 12, 1933)


''' namedtuple '''
Person = namedtuple('Person', ['name', 'age'])
p = Person('Bob', 77)

p._fields                # ('name', 'age')
p.name, p.age            # Bob 77
p._asdict()              # OrderedDict([('name', 'Bob'), ('age', 77)])
p._replace(name='Bill')  # Person(name='Bill', age=77)


''' list '''
[[0] for i in range(2)]        # одномерный массив
# [[0], [0]]

[([0] * 3) for i in range(5)]  # двумерный массив
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]


''' deque '''
q = deque()
q = deque([1, 2, 3])
q.appendleft(0)  # deque([0, 1, 2, 3])
q.popleft()      # 0

q = deque([1, 2], maxlen=2)
q.appendleft(0)  # deque([0, 1], maxlen=2)
q.append(2)      # deque([1, 2], maxlen=2)


''' set '''
xs, ys, zs = {1, 2}, {2, 3}, {3, 4}

set.union(xs, ys, zs)         # xs | ys | zs
# {1, 2, 3, 4}
set.intersection(xs, ys, zs)  # xs & ys & zs
# set()
set.difference(xs, ys, zs)    # xs - ys - zs
# {1}

frozenset()                   # неизменяемое множество


''' dict '''
d = dict(foo='bar')
# {'foo': 'bar'}
d1 = dict(d, boo='baz')  # копирование словаря
# {'boo': 'baz', 'foo': 'bar'}
d2 = dict.fromkeys(['foo', 'bar'], 0)
# {'foo': 0, 'bar': 0}
d3 = dict.fromkeys('abcd', 0)
# {'a': 0, 'b': 0, 'c': 0, 'd': 0}
d4 = {ch: [] for ch in 'abcd'}
# {'a': [], 'b': [], 'c': [], 'd': []}

d = {'foo': 'bar'}
d.setdefault('foo', '')  # 'bar'
d.setdefault('boo', 42)  # 42
# {'foo': 'bar', 'boo': 42}


'''defaultdict'''
dd = defaultdict(set, **{'a': {'b'}, 'b': {'c'}})
dd['c'].add('a')
# {'a': {'b'}, 'b': {'c'}, 'c': {'a'}}


'''OrderedDict'''  # порядок по добавлению
do = OrderedDict([('foo', 'bar'), ('boo', 42)])
list(do)  # ['foo', 'boo']


'''Counter'''
c = Counter(['foo', 'foo', 'foo', 'bar'])  # Counter({'foo': 3, 'bar': 1})
c['foo'] += 1                              # ({'foo': 4, 'bar': 1})
c.most_common(1)                           # [('foo', 4)]
c.subtract({'foo': 2})                     # Counter({'foo': 2, 'bar': 1})
