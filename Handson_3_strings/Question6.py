str1 = input("Enter the string: ")
lowercase = ""
uppercase = ""
for ch in str1:
    if ch.islower():
        lowercase = lowercase + ch
    else:
        uppercase = uppercase + ch
result = lowercase + uppercase
print(result)