#creating an empty set
b= set()
print(type(b))

# adding vvalu to an empty set
b.add(4)
b.add(5)
b.add(5)#adding value repeatedly does not changes a set
b.add((5,6,7))
#b.add({4:5})# cannot add list or dictonary
print(b)
# length of set
print(len(b))# print the lenghth of set
# removal of an item
b.remove(5) # removes 5 from sets
#b.remove(15) #throws an error
print(b.pop())
print(b)
