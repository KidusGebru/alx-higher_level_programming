#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) < 4 or len(sys.argv) > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        result = 0
        a = sys.argv[1]
        b = sys.argv[3]
        if sys.argv[2] == "+":
            result = add(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == "-":
            result = sub(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == "*":
            result = mul(int(sys.argv[1]), int(sys.argv[3]))
        elif sys.argv[2] == "/":
            result = div(int(sys.argv[1]), int(sys.argv[3]))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))
