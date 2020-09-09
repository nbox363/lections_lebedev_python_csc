# объявление своего исключения
class CSCEexception(Exception):
    pass


class TestFailure(CSCEexception):
    def __str__(self):
        return 'lecture test failed'
