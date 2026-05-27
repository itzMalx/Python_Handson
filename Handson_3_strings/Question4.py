str1 = input("Enter the string: ")
result = ""
for ch in str1:
    if ch.isalnum() or ch.isspace():
        result = result + ch
    else:
        result = result + "#"
print(result)