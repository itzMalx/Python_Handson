def safe_division(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Error: Division by zero!")
safe_division(10, 2)
safe_division(8, 0)