a = 33
b = 200
#if b > a:
  #print("b is greater than a")



############ elif *************
a = 33
b = 33
#if b > a:
 # print("b is greater than a")
#elif a == b:
#  print("a and b are equal")

#############  else ******************
a = 200
b = 33
#if b > a:
#  print("b is greater than a")
#elif a == b:
 # print("a and b are equal")
#else:
 # print("a is greater than b")

 ########### else without elif ***************
a = 200
b = 33
#if b > a:
 # print("b is greater than a")
#else:
 #  print("b is not greater than a")

#  short hand if ***********
a = 200
b = 33
#if a > b: print("a is greater than b")


# one lin else statement***********
a = 2
b = 330
#print("A") if a > b else print("B")


####### one line else statement with three conditions ************
a = 330
b = 330
#print("A") if a > b else print("=") if a == b else print("B")


#The _and_ keyword is a logical operator, and is used to combine conditional statements



a = 200
b = 33
c = 500
#if a > b and c > a:
 # print("Both conditions are True")

########### at least one condition is true  ************
a = 200
b = 33
c = 500
#if a > b or a > c:
#  print("At least one of the conditions is True")


  ############ nested if ************
x = 41

#if x > 10:
 # print("Above ten,")
  #if x > 20:
    #print("and also above 20!")
  #else:
  #  print("but not above 20.")

    ########### pass statement ***************
a = 33
b = 200

if b > a:
  pass

# having an empty if statement like this, would raise an error without the pass statement


