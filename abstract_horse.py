from abc import ABCMeta,abstractclassmethod
class animal(metaclass=ABCMeta):
    def __init__(self ,name ,age ,color) :
        self.name =name
        self.age =age
        self.color =color

    @abstractclassmethod
    def sound(self):
        pass
class horse(animal):
    def sound(self):
        return "ihihihi"
    
var =horse("spirit",3, "black")
print(var.sound())
