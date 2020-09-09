""" Iterators """


from itertools import islice


class Identity:
    def __getitem__(self, idx):  # становится итератором
        if idx > 5:
            raise IndexError(idx)
        return idx


list(Identity())  # [0, 1, 2, 3, 4, 5]

####################################################################################


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

####################################################################################


""" Generators """


def unique(iterable, seen=None):
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item

####################################################################################


def map(func, iterable, *rest):
    for args in zip(iterable, *rest):
        yield func(*args)

####################################################################################


def chain(*iterables):
    for iterable in iterables:
        for item in iterable:
            yield item

####################################################################################


def count(start=0):
    while True:
        yield start
        start += 1

####################################################################################


def enumerate_(iterable, start=0):
    return zip(count(start), iterable)

####################################################################################


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

####################################################################################


def g():
    res = yield
    print(f"Got {res}")
    res = yield 42
    print(f"Got {res}")

####################################################################################


def grep(pattern):
    print("Loking for {!r}".format(pattern))
    while True:
        line = yield
        if pattern in line:
            print(line)


gen = grep("Gotcha!")
next(gen)  # Loking for 'Gotcha!'
gen.send("This line doesn't have waht we're looking for")
gen.send("This one does. Gotcha!")  # This one does. Gotcha!

####################################################################################

""" Itertools """


xs = range(10)

list(islice(xs, 3))  # [1, 2, 3]

list(islice(xs, 3, None))  # [3, 4, 5, 6, 7, 8, 9]

list(islice(xs, 3, 8, 2))  # [3, 5, 7]
