string1 = input("Enter the string: ")
words = string1.split()
a = words[0]
b = words[1]
c = words[2]
print("Print String in default order:")
print("{} {} {}".format(a, b, c))
print("\nPrint String in Positional order:")
print("{1} {0} {2}".format(a, b, c))
print("\nPrint String in order of Keywords:")
print("{c} {b} {a}".format(a=a, b=b, c=c))