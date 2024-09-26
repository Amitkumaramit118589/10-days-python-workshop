class College:
    def _init_(self,n,loc):
        self.name=n
        self.location=loc
    def info(self):
        print(self.name+"is located in "+self.location)


class Department(College):
    def _init_(self,ids,n):
        self.id=ids
        self.name=n
        super()._init_(n,"GEC Vaishali")
    def info_d(self):
        print(self.id+"is a department of "+self.name)

D=Department("155","CSE(IoT)")
D.info_d()
D.info()
