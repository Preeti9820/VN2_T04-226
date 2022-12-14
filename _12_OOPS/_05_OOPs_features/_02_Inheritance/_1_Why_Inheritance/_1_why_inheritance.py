'''
Parent
Children

class Address:
    hno
    streetno
    colony,
    area,
    landmark,
    pincode,
    village,
    mandal,
    taluka,
    district,
    state


class Employee:
    int eid;
    String name;
    float sal;
    Address address;
        # 'hno,streeno,colony,area,landmark,pincode,village,mandal,taluka,district,stae'
'''

'''
is-a relationship    <SUB> is a <SUPER>

2 classes: 
    Super   - Sub* 
    Parent  - Child* 
    Base    - Derived 


A1:             Tiger, Lion, Cat, Dog 
    
    
A2:                      Animal
               |      |           |     |
              Tiger  Lion        Cat    Dog 


A3:                     Animal
                  |                   |
                Wild               Domestic
                |  |                 |     |
             Tiger Lion              Cat   Dog 
    
    

Without inheritance:
---------------------
Tiger, Lion, Cat, Dog 

A1:    Tiger        Lion              Cat         Dog 
        eating()    eating()           eating()   eating()   # Code duplication

With inheritance:
---------------------
A2:                   Animal
        Tiger   Lion         Cat    Dog 
    
                       Animal
                         eating()            # code reusability, avoids code duplication
             |        |           |       |  
         Tiger        Lion        Cat     Dog 
      
Inheritance => is-a relationship **
Aggregation => has-a relationship  # Controller-Service-DAO layer

Tiger is a Animal     - TRUE
Lion is a Animal      - TRUE
Cat is a Animal       - TRUE
Dog is a Animal       - TRUE
SEmployee is a Animal - FALSE 

   FileWriter
pdf excel ppt word

LED TV is a TV
LCD TV is a TV
Laptop is a TV

SOLID Principles :  Single responsibility Principle
'''

class Animal:

    def __init__(self):
        print("SUPER :: Animal constructor")

    def eating(self):
        print("SUPER :: Animal : eating")

class Tiger(Animal):   # Inheritance

    def __init__(self):
        print("SUB  :: Tiger constructor")

    def sleeping(self):
        print("SUB  :: Tiger sleeping")

print("--------super class object creation--------")
animal = Animal()
animal.eating()
# animal.sleeping() # ERROR

print("--------sub class object creation--------")
tiger = Tiger()   # Tiger tiger = new Tiger()  int x = 10
tiger.sleeping()  # sub class specific method
tiger.eating()    # inherited super class method

class Dog(Animal):

    def __init__(self):
        print("SUB :: Dog constructor")

    def bark(self):
        print("SUB :: Dog Barking")

print("--------DOG : sub class object creation--------")
dog = Dog()
dog.eating()
dog.bark()
dog.xyz()



'''
# Aggregation has-a relationship

# Employee has a Address

class Address:
    def __init__(self, hno, flatno, area, line, city, pincode, state):
        pass

class Employee:
    def __init__(self, id, name, sal, address):
        self.id = id
        self.name = name
        self.sal = sal
        self.address = address

addr = Address(123,205,'Marthahalli','2ndline','Bangalore',560037,'Karnataka')
madhu = Employee(100, 'Madhu N', 10000, addr)

# Employee has a address
'''