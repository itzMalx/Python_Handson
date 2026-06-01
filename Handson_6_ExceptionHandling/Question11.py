try:
    m = int(input("Enter Maths mark: "))
    p = int(input("Enter Physics mark: "))
    c = int(input("Enter Chemistry mark: "))
    total = m + p + c
    if m >= 65 and p >= 55 and c >= 50 and total >= 180:
        print("Eligible")
    else:
        raise Exception("Not Eligible")
except Exception as e:
    print(e)