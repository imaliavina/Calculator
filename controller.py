from division_integer import division_int
from division_remainder import division_rem
from summa import summa
from difference import diff
from multiplication import mult
from division import division
from init import init_operand, init_operator
from logging import log


def to_do(op, x, y):

    operation = init_operator(op)

    result = operation(x, y)
    print_result(result)
    log(result, op)

    return result

















def print_result(result):
    print(f'Результат операции: {result}')


