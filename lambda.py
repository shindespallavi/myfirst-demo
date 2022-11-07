x = lambda a : a + 10
#print(x(5))

################ multiple argument **************
x = lambda a, b : a * b
#print(x(5, 6))

x = lambda a, b, c : a + b + c
#print(x(5, 6, 2))



#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

#print(mydoubler(11))



#same function definition to make both functions, in the same program:

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

#print(mytripler(11))



#use the same function definition to make both functions, in the same program:


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

#print(mydoubler(11))
#print(mytripler(11))





