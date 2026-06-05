students = { "25MCA001": 77, "25MCA009": 60,"25MCA025": 99, "25MCA007": 84,"25MCA012": 45,"25MCA021": 86,"25MCA032": 83,   "25MCA018": 40,"25MCA014": 67
}
max_marks = max(students.values())
min_marks = min(students.values())
print("Maximum:", max_marks)
for usn, mark in students.items():
    if mark == max_marks:
        print(usn)

print("Minimum:", min_marks)
for usn, mark in students.items():
    if mark == min_marks:
        print(usn)

distinction = []
merit = []
passed = []
failed = []
distinction=[]
for usn, mark in students.items():
    if 86 <= mark <= 100:
        distinction.append(usn)
    elif 76 <= mark <= 85:
        merit.append(usn)
    elif 60 <= mark <= 75:
        passed.append(usn)
    else:
        failed.append(usn)

print("Distinction:", len(distinction), distinction)
print("Merit:", len(merit), merit)
print("Pass:", len(passed), passed)
print("Fail:", len(failed), failed)

avg = sum(students.values()) / len(students)

print("Class Average:", round(avg, 2))

below_avg = []

for usn, mark in students.items():
    if mark < avg:
        below_avg.append(usn)

print("Below Average:", below_avg)

leaderboard = sorted(students.items(), key=lambda x: x[1], reverse=True)

print("-----Leaderboard------")
for usn, mark in leaderboard:
    print(usn, ":", mark)
