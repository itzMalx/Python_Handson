text = input("Enter any String: ")
words = text.split()
smallest = words[0]
for word in words:
    if len(word) < len(smallest):
        smallest = word
print("Smallest word:", smallest)