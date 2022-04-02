'''
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
'''
'''''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
'''''
#Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#create student class
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname) #get all attributes from parent 
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
y = Student("Mike", "Olsen", 2019)
y.welcome()
