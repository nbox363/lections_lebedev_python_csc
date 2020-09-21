import itertools
import doctest
import unittest



def rle(iterable):
    ''' Пример для тестирования '''
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)


>>> list(rle('mississippi'))
# [('m', 1), ('i', 1), ('s', 2), ('i', 1),
#  ('s', 2), ('i', 1), ('p', 2), ('i', 1)]


# ###################################################################################


''' doctest '''


def rle(iterable):
    '''
    >>> list(rle(''))
    []
    >>> list(rle('mississippi'))
    # doctest: +NORMALIZE_WHITESPACE
    [('m', 1), ('i', 1), ('s', 2), ('i', 1),
     ('s', 2), ('i', 1), ('p', 2), ('i', 1)]
    '''
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)


if __name__ = '__main__':
    doctest.testmod()


# ###################################################################################


''' unittest '''


class TestHomework(unittest.TestCase):
    def test_rle(self):
        self.assertEqual(rle('mississippi'), [...])

    def test_rle_empty(self):
        self.assertEqual(list(rle('')), [])


if __name__ == '__main__':
    unittest.main()