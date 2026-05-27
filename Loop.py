num = int(input("Enter a number: "))
fact = 1
for i in [1, 2, 3, 4, 5]:
    if i <= num:
        fact = fact * i
print("Factorial is:", fact)