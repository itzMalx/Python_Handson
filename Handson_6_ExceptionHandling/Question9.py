n = input("Enter a number: ")
if n.isdigit():
    rev = n[::-1]
    if n == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")
else:
    print("Enter only integer numbers")