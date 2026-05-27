tuple1 = ('Manjeet', 'Nikhil', 'Akshat')
tuple2 = (' Singh', ' Meherwal', ' Garg')
result = ()
for i in range(len(tuple1)):
    result = result + (tuple1[i] + tuple2[i],)
print("The concatenated tuple:", result)