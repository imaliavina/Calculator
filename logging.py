from datetime import datetime as dt


def operator_name(op):
    names = {'//': 'integer division',
             '%': 'remainder division',
             '*': 'multiplication',
             '-': 'difference',
             '+': 'sum',
             '/': 'division'}

    return names[op]


def log(result, op):
    time = dt.now()
    with open('log.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{time.hour}:{time.minute}      операция: {operator_name(op)}      результат: {result}\n')