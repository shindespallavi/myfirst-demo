class MyClass:
  x = 5

#print(MyClass)



################ creating an object *********************
class MyClass:
  x = 5

p1 = MyClass()
#print(p1.x)

################### the _init_() function
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

#print(p1.name)
#print(p1.age)

############# the _str_() function   without the string *********
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

#print(p1)


##############The string representation of an object WITH the __str__() function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

#print(p1)


################# object method *********************
#class Person:
  #def __init__(self, name, age):
    #self.name = name
    #self.age = age

  #def myfunc(self):
   # print("Hello my name is " + self.name)

#p1 = Person("John", 36)
#p1.myfunc()



####################### the self parameter**********************
#class Person:
 # def __init__(mysillyobject, name, age):
  #  mysillyobject.name = name
   # mysillyobject.age = age

  #def myfunc(abc):
    #print("Hello my name is " + abc.name)

#p1 = Person("John", 36)
#p1.myfunc()


#################### modifying object properties *********************
#class Person:
 # def __init__(self, name, age):
  #  self.name = name
    #self.age = age

  #def myfunc(self):
  #  print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40

#print(p1.age)


################# delete object properties *************
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1.age

print(p1.age)

