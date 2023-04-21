class Person:
    def __init__ (self, name, lastname, age):
        self.name = name
        self.__lastname = lastname #private
        self.age = age
    
    def get_lastname(self):
        return self.__lastname

    def great(self):
        print(f"Hello, My name is {self.name} and i am {self.age} years old")

person1 = Person("Ezequiel", "Bamio", 22)
person1.great()
print(person1.name)
print(person1.get_lastname())

