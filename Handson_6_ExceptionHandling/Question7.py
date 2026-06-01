try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op = input("Enter operator (+,-,*,/): ")
    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        if a == 0 or b == 0:
            print("Multiplication with 0 is not allowed")
        else:
            print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Division by zero is not allowed")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operator")
except ValueError:
    print("Only numbers are allowed")