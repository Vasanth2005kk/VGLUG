class student:
    def __init__(self,name,roll_namber):
        self.name=name
        self.roll_namber=roll_namber
    def student_details(self):
        print("student name:",self.name)
        print("student roll_number:",self.roll_namber)
std_1=student("vasanth",261444122)
std_1=student("shandiya",261444123)
std_1.student_details()
