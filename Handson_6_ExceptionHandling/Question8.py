class InputNotANumberException(Exception):
    pass
class DivisionByZeroException(Exception):
    pass
class InvalidMultiplierException(Exception):
    pass
try:
    op = input("Enter operation (+,-,*,/): ")
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not a.isdigit() or not b.isdigit():
        raise InputNotANumberException
    a = int(a)
    b = int(b)
    if op == "+":
        print("Output:", a + b)

    elif op == "-":
        print("Output:", a - b)
    elif op == "*":
        if a == 0 or b == 0:
            raise InvalidMultiplierException
        print("Output:", a * b)
    elif op == "/":
        if b == 0:
            raise DivisionByZeroException
        print("Output:", a / b)
except InputNotANumberException:
    print("Error: Input must be a number.")
except DivisionByZeroException:
    print("Error: Division by zero is not allowed.")
except InvalidMultiplierException:
    print("Error: Multiplication by zero is not allowed.")