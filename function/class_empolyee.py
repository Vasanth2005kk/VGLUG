class empolyee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salay=salary
    def getempolyee(self):
        print("empolyee ID:",self.id)
        print("empolyee name:",self.name)
        print("empolyee salary:",self.salay)
emp1=empolyee("1234567","vasanth",50000)
emp1.getempolyee()