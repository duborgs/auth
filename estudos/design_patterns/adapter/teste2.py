
class Adapter: 

    def __init__(self, obj, **adapted_methods): 
        self.obj = obj 
        self.__dict__.update(adapted_methods)
        
    def __getattr__(self, attr): 
      return getattr(self.obj, attr)
   
class Car:
    
    def __init__(self) -> None:
        pass
    
    def type_veicle():
        print('Car')
        
car = Adapter(Car, exect = Car.type_veicle)

car.exect()
