listA=[]
n=int(input("Enter number of elements in the list:"))
for i in range(0,n):
    print("Enter element No-{}:".format(i+1))
    elm=int(input())
    listA.append(elm)
    print("The entered list is:/n",listA)