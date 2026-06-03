import re
text="Alan Turning was a pioneer of theoretical computer science and artiical intelligence.He was born on 23 june 1912 in Maiada Vale,London"
res=re.sub('theoretical','practical',text)
print("Result={}".format(res))
