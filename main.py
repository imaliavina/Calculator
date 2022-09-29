import controller as c
from input import input_operand, input_op, input_complex_operand
from init import init_operand, init_complex_operand


if __name__ == '__main__':

    with open('log.txt', 'r+') as f:
        f.truncate(0)

    answer = input('Вещественные - r или комплексные - c?')

    if answer == 'r':

        a = input_operand()
        x = init_operand(a)

        while True:

            op = input_op()
            if op == 'e':
                break
            else:
                b = input_operand()
                y = init_operand(b)
                x = c.to_do(op, x, y)

    elif answer == 'c':

        a, b = input_complex_operand()
        x = init_complex_operand(a, b)

        while True:

            op = input_op()
            if op == 'e':
                break
            else:
                a, b = input_complex_operand()
                y = init_complex_operand(a, b)
                x = c.to_do(op, x, y)

    else:
        print('Неправильный ответ')







