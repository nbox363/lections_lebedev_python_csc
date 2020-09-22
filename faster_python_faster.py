''' В качестсве примера используется умножение матриц '''


import random


class Matrix(list):
    @classmethod
    def zeros(cls, shape):
        n_rows, n_cols = shape
        return cls([[0] * n_cols for i in range(n_rows)])

    @classmethod
    def random(cls, shape):
        M, (n_rows, n_cols) = cls(), shape
        for i in range(n_rows):
            M.append(
                [random.randint(-255, 255) for j in range(n_cols)]
                )
        return M

    @property
    def shape(self):
        return ((0, 0) if not self else (len(self), len(self[0])))


def matrix_product(X, Y):
    n_xrows, n_xcols = X.shape
    n_yrows, n_ycols = Y.shape
    Z = Matrix.zeros((n_xrows, n_ycols))
    for i in range(n_xrows):
        for j in range(n_xcols):
            for k in range(n_ycols):
                Z[i][k] += X[i][j] * Y[j][k]
    return Z


# ###################################################################################


''' Измерить время работы '''


import timeit


setup = '''
from faster_python_faster import Matrix, \
    matrix_product
shape = 64, 64
X = Matrix.random(shape)
Y = Matrix.random(shape)
'''

timeit.timeit('matrix_product(X, Y)', setup, number=10)


# ###################################################################################


def matrix_product_v2(X, Y):
    ''' Запоминает значение X[i] и Z[i] 
        код делает меньше запросов по индексу
    '''
    n_xrows, n_xcols = X.shape
    n_yrows, n_ycols = Y.shape
    Z = Matrix.zeros((n_xrows, n_ycols))
    for i in range(n_xrows):
        Xi = X[i]
        for k in range(n_ycols):
            acc = 0
            for j in range(n_xcols):
                acc += Xi[j] * Y[j][k]
            Z[i][k] = acc
    return Z


# ###################################################################################


def matrix_product_v3(X, Y):
    n_xrows, n_xcols = X.shape
    n_yrows, n_ycols = Y.shape
    Z = Matrix.zeros((n_xrows, n_ycols))
    for i in range(n_xrows):
        Xi, Zi = X[i], Z[i]
        for k in range(n_ycols):
            acc = 0
            for j in range(n_xcols):
                acc += Xi[j] * Y[j][k]
            Zi[k] = acc


# ###################################################################################


def matrix_product_v4(X, Y):
    ''' замена цилка на выражение генератор '''
    n_xrows, n_xcols = X.shape
    n_yrows, n_ycols = Y.shape
    Z = Matrix.zeros((n_xrows, n_ycols))
    for i in range(n_xrows):
        Xi, Zi = X[i], Z[i]
        for k in range(n_ycols):
            Z[i] = sum(
                Xi[j] * Y[j][k] for j in range(n_xcols)
            )
    return Z
