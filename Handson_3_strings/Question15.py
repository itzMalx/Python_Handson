s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
x = s1[0] + s2[0]
y = s1[len(s1)//2] + s2[len(s2)//2]
z = s1[-1] + s2[-1]
result = x + y + z
print(result)