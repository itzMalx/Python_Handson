String = input("Enter the String:")
lower=upper=others=0
for i in String:
    if(i.islower()):
        lower+=1
    elif(i.isupper()):
        upper+=1
    else:
        others+=1
print("Lower case letters:",lower)
print("Upper case letters:",upper)
print("Non-letters:",others)