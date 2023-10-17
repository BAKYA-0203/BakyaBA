class Animals:
    def fun1(self):
        print("This animal name is DOG")
class b(Animals):
    def fun2(self):
        print("This animal name is CAT")
class c(b):
    def fun3(self):
        print("This animal name is RABBIT")
class d(c,b):
    def fun4(self):
        print("Animals")
obj=d()
obj.fun4()
obj.fun1()
obj.fun2()
obj.fun3()
