dict = {"25MCA001": 77, "25MCA009": 60, "25MCA025": 99, "25MCA012":45,
        "25MCA007":84,"25MCA021":86, "25MCA032":83,
        "25MCA018":40, "25MCA014":67}
highest = 0
lowest = 100
pass_count = 0
fail_count = 0
dist = []
merit = []
failed_students = []

for key, value in dict.items():

    if value > highest:
        highest = value

    if value < lowest:
        lowest = value

    if value >= 86:
        dist.append(value)

    elif 76 <= value <= 85:
        merit.append(value)

    elif 60 <= value <= 75:
        pass_count += 1

    else:
        fail_count += 1
        failed_students.append(value)

print("Highest Mark :", highest)
print("Lowest Mark :", lowest)
print("Distinction :", len(dist), "->", dist)
print("Merit :", len(merit), "->", merit)
print("Pass Count :", pass_count)
print("Fail Count :", fail_count)
print("Failed Marks :", failed_students)
average = sum(dict.values()) / len(dict)

print("Average Mark :", average)

print("----- LeaderBoard-----")
print(highest)