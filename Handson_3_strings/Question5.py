text = input("Enter the string: ")
words = text.split()
print("Alphanumeric words are:")
for word in words:
    if word.isalnum() and not word.isalpha() and not word.isnumeric():
        print(word)