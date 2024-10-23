class Vehicle:
    def __init__(self,brand,start):
        self._brand=brand
        self._start=start
       
    def display_info(self):
        return f"The {self._brand} vehicle is {self._start}"
class Car(Vehicle):
    def __init__(self,brand,start,color):
        #kế thừa hàm khởi tạo từ class cha Vehicle

        super().__init__(brand,start)
        self._color=color
    def display_info(self):
        parentClass=super().display_info()
        return f"{parentClass}, the color is {self._color}"

brand=input("Hãy nhập hãng của xe: ")
start=input("Hãy nhập tình trạng của xe: ")
color=input("Hãy nhập màu sắc của xe: ")
car=Car(brand,start,color)    
print(car.display_info())



        


