class Example:
    def method(self,a,b=None):
        if b is None:
            print(f"Single arugment:{a}")
        elif isinstance(a,int)and isinstance(b,int):
            print(f"Two integers:{a},{b}")
        elif isinstance(a,str)and isinstance(b,str):
            print(f"Mixd types:{a},{b}")
obj = Example()
obj.method(1)
obj.method(1,2)
obj.method("hello","world")
obj.method(1,"world")