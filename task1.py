class Student():
    def __init__(self,name,last_name,age,):
        self.name = name 
        self.last_name = last_name 
        self.age = age

    def _print_arg(self):
        print(self.name,self.last_name,self.age)

student1 = Student(
    "Kairat","Sultanbekov","20"
)
student1._print_arg()
    

