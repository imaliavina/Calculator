from division_integer import division_int
from division_remainder import division_rem
from summa import summa
from difference import diff
from multiplication import mult
from division import division


def init_operand(a):
    global x
    x = a

    return x


def init_complex_operand(a, b):
    global x
    x = complex(a, b)

    return x

def init_operator(op):

    operations = {'//': division_int,
                  '%': division_rem,
                  '*': mult,
                  '-': diff,
                  '+': summa,
                  '/': division}

    return operations[op]





