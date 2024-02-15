import datetime

class Student:
    def __init__(self, id_number, name, course):
        self.id_number = id_number
        self.name = name
        self.course = course
    
    def __str__(self) -> str: 
        return (f"{self.id_number} - {self.name} - {self.course}")
        
    def validate_info(self) -> None:
        name_letters = self.name.replace(" ", "").isalpha()
        if len(self.id_number) != 9 or not name_letters:
            print("Student information is not valid.")
        else:
            print("Student information is valid.")
          
test_student = input("Testing Student: ").split(' - ')
id_number, name, course = test_student[0], test_student[1], test_student[2]
student1 = Student(id_number, name, course)
student1.validate_info()

current_date_time = datetime.datetime.now()
print(current_date_time)




