n=int(input("Enter a number: "))
dict={5:'five',9:'nine',3:'three',2:'two',0:'zero',1:'one'}
if n in dict:
    print(dict[n])
else:
    print("number not found")