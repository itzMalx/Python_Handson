myobject=open("myfile.txt",'w')
lines=['Hello everyone\n',"This is the #line"]
myobject.writelines(lines)
myobject.close()
print("Now reading the contents of the files:")
foobject=open("testfile.txt",'r')
for str in object:
    print(str)
foobject.close()