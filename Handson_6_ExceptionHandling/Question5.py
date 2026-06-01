try:
    person = {"age": 30}
    print(person["name"])
except KeyError:
    print("Error: Key not found!")