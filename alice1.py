def increment(list2):
    print("\nID of list inside function before assignment:", id(list2))
    list2 = [1, 2, 3, 4, 5]
    for i in range(0, len(list2)):
        list2[i] += 5
    print("ID of list inside function after assignment:", id(list2))
    print("The list inside the function after assignment is:")
    print(list2)
list1 = [10, 20, 30, 40, 50]
print("ID of list before function call:", id(list1))
print("The list before function call:")
print(list1)
increment(list1)
print("\nID of list after function call:", id(list1))
print("The list after function call:")
print(list1)