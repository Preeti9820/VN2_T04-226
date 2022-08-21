'''class Employee:
    # 1. STATE  # Declaration
    def __init__(self, empid, name, sal):
        self.empid = empid
        self.name = name
        self.sal = sal

    # 2. BEHAVIOR  ---> Method
    def get_einfo(self):
        print("Self : ", self)
        print("Employee details are ", self.empid, self.name, self.sal)
madhu = Employee(100, 'Madhu Nettem', 15000)  # Initialization
print("Madhu : ", madhu)
madhu.get_einfo()



class Television:
    # STATE
    def __init__(self, tid, name, price, color):
        self.tid = tid
        self.name = name
        self.price = price
        self.color = color

    # BEHAVIOR
    def get_telinfo(self):
        print("Television info : ", self.name, self.price, self.color)

samsung = Television('L0001', 'Samsung', 25400, 'Black')
samsung.get_telinfo()



class student:
    def __init__(self,sname,sroll,sclass):
        self.sname = sname
        self.sroll = sroll
        self.sclass = sclass

    def get_sinfo(self):
        print("student name :",self.sname,self.sclass,self.sroll)

preeti = student('preeti',226,'10th')
preeti.get_sinfo()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Preeti", 24)

print(p1.name)
print(p1.age)



class Moter:
    def __init__(self,bname,rnum,millage,age):
        self.bname = bname
        self.rnum = rnum
        self.millage = millage
        self.age = age
    def get_list(self):
        print("The moter info is:",self.bname,self.rnum,self.millage,self.age)

bike = moter('bulet','234567','60/km','2')
bike.get_list()


class Snaks:
    def __init__(self,type,name,quantity,price):
        self.type = type
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_info(self):
        print("Type is:",self.type,"name:",self.name,"Quantity:",self.quantity,"& price:",self.price)

s1 = Snaks('sweet','britania','200gm','35/-')
s1.get_info()
s2 = Snaks('sweet','gooday','100gm','15/-')
s2.get_info()
s3 = Snaks('salty','monaco','200gm','40/-')
s3.get_info()
s4 = Snaks('salty','potata','200gm','25/-')
s4.get_info()
s5 = Snaks('sweet','orio','50gm','15/-')
s5.get_info()



class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


#"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
#"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)


class Student:
    def __init__(self):
        self.name = 'Preeti'
        self.age = 24
        self.marks = 567

    def talk(self):
        print("Hi , I am ,",self.name)
        print("My age is",self.age)
        print("My marks are",self.marks)
x= Student()
x.talk()

number= list(input("enter the number"))
def reve():
    global number
    rev = number.reverse()
    print("reverse is:",rev)

x=reve()
print(x)
'''


class Reverse:
    def __init__(self):
        self.string = input("Enter the string")
    def reversing(self):
        rev = ""
        for i in self.string:
            rev = i + rev
        print(rev)
obj = Reverse()
obj.reversing()
