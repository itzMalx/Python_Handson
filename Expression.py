#without using comprehension
ele=[]
for x in range(5):
    ele.append(x**2)
print(ele)
#with using comprehension
ele=[x**2 for x in range(5)]
print(ele)