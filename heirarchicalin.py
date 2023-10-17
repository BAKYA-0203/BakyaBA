class parent:
    def fun1(self):
        print("My Family")
class fname(parent):
    def fun2(self):
        print("Father Name : Kiran")
class mname(parent):
    def fun3(self):
        print("Mother Name : Keerthi")
class son(parent):
    def fun4(self):
        print("Im Karan")
a=son()
b=mname()
c=fname()
a.fun1()
a.fun4()
b.fun3()
c.fun2()
