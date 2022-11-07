############### creating a parent class *********************
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  #def printname(self):
   # print(self.firstname, self.lastname)

x = Person("John", "Doe")
#x.printname()


####################### child class *******************
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  #def printname(self):
   # print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
#x.printname()


#################### the _init_() function
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  #def printname(self):
    #print(self.firstname, self.lastname)

#class Student(Person):
  #def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
#x.printname()


################### the super() function
#class Person:
 # def __init__(self, fname, lname):
    #self.firstname = fname
    #self.lastname = lname

  #def printname(self):
    #print(self.firstname, self.lastname)

#class Student(Person):
  #def __init__(self, fname, lname):
    #super().__init__(fname, lname)

#x = Student("Mike", "Olsen")
#x.printname()


####################### add properties *****************
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
#print(x.graduationyear)



