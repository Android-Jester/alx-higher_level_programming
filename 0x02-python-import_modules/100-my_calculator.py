#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    if argc < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        exit(1)
    operators = "+-*/"
    operator = argv[1]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[0])
    b = int(argv[2])
    operator_funcs = [add, sub, mul, div]
    func = operator_funcs[operators.index(operator)]
    print("{} {} {} = {}".format(a, operator, b, func(a, b)))

