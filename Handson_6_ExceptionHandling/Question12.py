try:
    n = int(input("Enter a number: "))
    square = n * n
    print(f"The square of {n} is {square}")
except ValueError:
    print("Error: Invalid input.")
    print("Please enter a valid number.")
finally:
    print("Execution complete")