#!/usr/bin/python3
import calculator_1
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
<<<<<<< HEAD
    operator = sys.argv[2] 
=======
    operator = sys.argv[2]
>>>>>>> edb4d581fc3054be668a7892f69d16b9ae59895f
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif operator == '+':
        result = calculator_1.add(a, b)
    elif operator == '-':
        result = calculator_1.sub(a, b)
    elif operator == '*':
        result = calculator_1.mul(a, b)
    elif operator == '/':
        result = calculator_1.div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
