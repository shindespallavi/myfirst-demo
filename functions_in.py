#def my_function():
  #print("Hello from a function")

#my_function()

############## passing an argument ********
#def my_function(fname):
  #print(fname + " Refsnes")

#my_function("Emil")
#my_function("Tobias")
#my_function("Linus")




################## number of arguments **************
#def my_function(fname, lname):
 # print(fname + " " + lname)

#my_function("Emil", "Refsnes")




################## arbitery arguments *arg *********************
#def my_function(*kids):
 # print("The youngest child is " + kids[2])

#my_function("Emil", "Tobias", "Linus")


##################### key word arguments ******************
#def my_function(child3, child2, child1):
 # print("The youngest child is " + child3)

#my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



#################### arbitary keyword ** kwargs *********************
#def my_function(**kid):
 # print("His last name is " + kid["lname"])

#my_function(fname = "Tobias", lname = "Refsnes")


########### defailt parameter value *****************
#def my_function(country = "Norway"):
 # print("I am from " + country)

#my_function("Sweden")
#my_function("India")
#my_function()
#my_function("Brazil")



#############3 passing a list as an argument **********************
#def my_function(food):
 # for x in food:
  #  print(x)

#fruits = ["apple", "banana", "cherry"]

#my_function(fruits)



#############3333 return values ***********
#def my_function(x):
 # return 5 * x

#print(my_function(3))
#print(my_function(5))
#print(my_function(9))


################ pass statement ***********
def myfunction():
  pass


############### recursion method *************************
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
