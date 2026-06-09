L=int(input("Enter Lower Limit"))
U=int(input("Enter Upper Limit"))
print("The Prime numbers between",L,"and","U","are:")
for num in range(L,U+1):
    if num>1:
        for i in range(2,num):
            if(num%1)==0:
                break
            else:
                print(num)