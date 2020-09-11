try:
    something_dangerous()
except (ValueError, ArithmeticError):
    pass
except TypeError as e:  # 'e' существует только внутри блока except
    pass


# ###################################################################################


BaseException.__subclasses__()  # базовый класс для встроенных исключений
# [<class 'Exception'>, <class 'GeneratorExit'>, <class 'SystemExit'>, <class 'KeyboardInterrupt'>]


# ###################################################################################


class CSCEexception(Exception):    # объявление своего исключения
    pass


class TestFailure(CSCEexception):  # наследуем от своего исключения
    def __str__(self):
        return 'lecture test failed'


# ###################################################################################


'''Исключение возникло в результате другого'''
try:
    {}['foobar']
except KeyError as e:
    raise RuntimeError('Oooops!') from e


# ###################################################################################


'''finaly'''
try:
    handle = open('example.txt', 'wt')
    try:
        do_something(handle)
    finally:
        handle.close()
except IOError as e:
    print(e, file=sys.stderr)


# ###################################################################################


'''else'''
try:
    handle = open('example.txt', 'wt')
else:  # выполняется если исключения не было
    report_success(handle)
except IOError as e:
    print(e, file=sys.stderr)
