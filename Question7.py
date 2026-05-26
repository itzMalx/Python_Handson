currentNumber = int(input("Enter a number: "))
if currentNumber % 2 != 0:
    currentNumber = (3 * currentNumber) + 1
else:
    currentNumber = currentNumber
print(currentNumber)