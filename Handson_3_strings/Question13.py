s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s2 = s2[::-1]
s3 = ""
length = min(len(s1), len(s2))
for i in range(length):
    s3 = s3 + s1[i] + s2[i]
s3 = s3 + s1[length:] + s2[length:]
print("Third string is:", s3)