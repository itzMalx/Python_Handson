def multiply(a, b):
    try:
        result = a * b
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError
        print(result)
    except TypeError:
        print("Error: Invalid operand type!")
multiply(3, 4)
multiply("3", 4)