class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def introduce(self):
        return f"Tôi tên là {self._name}, {self._age} tuổi"
class Student(Person):
    def __init__(self,name,age,student_id,gpa):
        #kế thừa hàm khởi tạo từ class cha Person
        super().__init__(name,age)
        self._student_id=student_id
        self._gpa=gpa
    def display_info(self):
        parentClass=super().introduce()
        return f"{parentClass}, mã số sinh viên là {self._student_id} với điểm trung bình {self._gpa}"
    def get_grade(self):
        if self._gpa >= 3.6:
            print("Học lực: Xuất sắc")
        elif self._gpa >= 3.2:
            print("Học lực: Giỏi")
        elif self._gpa >= 2.5:
            print("Học lực: Khá")
        elif self._gpa < 2.5:
            print("Học lực: Trung bình")
        


name=input("Hãy nhập tên sinh viên: ")
age=input("Hãy nhập tuổi sinh viên: ")
student_id=input("Hãy nhập mã sinh viên: ")
gpa=float(input("Hãy nhập điểm trung bình của sinh viên: "))
student=Student(name,age,student_id,gpa)
print(student.display_info())
student.get_grade()