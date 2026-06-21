
# *Classes,Objects,Attributes

class Book:
    pass

book1 = Book()
book1.title = "Python Basics"
book1.pages = 300
print(book1.title)
print(book1.pages)


class Employee:
    pass

employee1 = Employee()
employee1.name = "jack"
employee1.salary = "100000rs"
employee1.department = "IT"
print(employee1.name, employee1.salary, employee1.department)


# *Constructors,Methods

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

book1 = Book("Python", 500)
print(book1.title,book1.pages)

class Employee:
    def __init__(self,name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

employee = Employee("Jim", "200000Rs", "Finance")
print(employee.name, employee.salary, employee.department)

# *Methods, Encapsulation
    
class Person:
    def __init__(self, name="Unknown"):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

person = Person("Anas")
person.introduce()


class Calculator:
    def __init__(self):
        pass

    def add(self, a,b):
        return a + b
    
calc = Calculator()
print(calc.add(7 ,3))


class BankAcount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def show_balance(self):
        print(f"Balance: {self.balance}")

bank = BankAcount(1000)
bank.deposit(300)
bank.show_balance()


class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.salary = salary

    def give_raise(self,amount):
        self.salary = self.salary + amount

    def show_details(self):
        print(f"Name: {self.__name}\nSalary: {self.salary}")

emp = Employee("john", 100000)
emp.__name = "anas" # name won't change cause of Encapsulation with __ in name
emp.give_raise(10000)
emp.show_details()
        

# *Inheritance

class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade
stu = Student("anas", 10)
print(stu.name, stu.grade)
        

class Vehicle:
    def __init__(self,brand):
        self.brand = brand
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
car = Car("Toyota", "Avalon")
print(car.brand, car.model)


class Employee:
    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self, name, salary,department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        print(f"Name: {self.name}\nSalary: {self.salary}\nDepartment: {self.department}")

man = Manager("john",100000, "IT")
man.show_details()


# *Polymorphism

class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def introduce(self):
        print("I am a student")
per = Person()
stu = Student()
per.introduce()
stu.introduce()


class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    
shape = Shape()
rec = Rectangle(9,3)
print(shape.area(), rec.area())


class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is writing code")

class Designer(Employee):
    def work(self):
        print("Designer is creating designs")

emp = Employee()
dev = Developer()
designer = Designer()
emp.work()
dev.work()
designer.work()