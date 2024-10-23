class Animal:
    #constructor: khởi tạo
    def __init__(self,_name,_species):
        self.name=_name
        self.species=_species

    def display_info(self):
        return f"{self.name} is a {self.species}"
    
class Person(Animal):
    def __init__(self, _name,_species,_job):
        #kế thừa hàm khởi tạo từ class cha Animal
        super().__init__(_name,_species)
        self.job=_job
    def display_info(self):
        parentClass=super().display_info()
        return f"{parentClass} and doing {self.job}"

tommy=Person("Tommy","Human","Doctor")
print(tommy.display_info())
    

dog=Animal("Alex","Dog")
print(dog.name)
print(dog.species)
print(dog.display_info())