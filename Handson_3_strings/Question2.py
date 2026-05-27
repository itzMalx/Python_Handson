str1 = input("Enter the string: ")
word = input("Enter the substring: ")
position = str1.rfind(word)
if position != -1:
    print("Last occurrence of", word, "starts at index", position)
else:
    print("Substring not found")