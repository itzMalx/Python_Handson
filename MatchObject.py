import re 
text="Alan Turing was a pioneer of theoretical computer scienece and Turing artificial intelligence. he was born on 23 june 1912 in maida vale, London"
res=re.search('computer',text)
print("Match object ={}",format(res))
print("--"*30)
print("group method output =",res.group())
print("--"*30)
print("start method output=",res.start())
print("--"*30)
print("end method output=",res.end())
print("--"*30)
print("span method output=",res.re)
print("--"*30)
print("string attribute output=",res.string)
print("--"*30)
text=r'search\\in the string'
res=re.search(r"\\",text)
print("With r as prefix=",res)