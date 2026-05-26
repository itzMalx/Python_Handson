#num=2
#def demo():
    #num=num*2
    #print("In Functin num=",num)
    #demo()
num=2
def demo():
    global num
    num=num*2
    print("In Function=",num)
demo()