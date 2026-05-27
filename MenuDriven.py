list1 = []
while True:
    print("\n1.Append an element")
    print("2.Insert an element")
    print("3.Append a list to the given list")
    print("4.Modify an existing element")
    print("5.Delete an existing element from its position")
    print("6.Delete an existing element with a given value")
    print("7.Sort the list in ascending order")
    print("8.Sort the list in descending order")
    print("9.Display the list")
    print("10.Exit")
    num = int(input("Enter your choice : "))
    if num == 1:
        element = input("Enter element to add : ")
        list1.append(element)
        print("List :", list1)
    elif num == 2:
        position = int(input("Enter position : "))
        element = input("Enter element : ")
        list1.insert(position, element)
        print("List :", list1)
    elif num == 3:
        new_list = input("Enter elements separated by space : ").split()
        list1.extend(new_list)
        print("List :", list1)
    elif num == 4:
        position = int(input("Enter position to modify : "))
        element = input("Enter new value : ")
        list1[position] = element
        print("List :", list1)
    elif num == 5:
        position = int(input("Enter position to delete : "))
        list1.pop(position)
        print("List :", list1)
    elif num == 6:
        element = input("Enter element to remove : ")
        list1.remove(element)
        print("List :", list1)
    elif num == 7:
        list1.sort()
        print("Ascending order :", list1)
    elif num == 8:
        list1.sort(reverse=True)
        print("Descending order :", list1)
    elif num == 9:
        print("Current List :", list1)
    elif num == 10:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")