try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        raise Exception("Enter only positive numbers")
    total = 0
    for i in range(1, n + 1):
        total += 1 / (i ** i)
    print(round(total, 5))
except Exception as e:
    print("Exception:", e)