def get_positive_integer():
    try:
        num = int(input("Enter a positive integer: "))
        if num > 0:
            print(num)
        else:
            print("Error: Invalid input! Please enter a positive integer.")
    except ValueError:
        print("Error: Invalid input! Please enter a positive integer.")
get_positive_integer()