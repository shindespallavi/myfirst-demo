#***************creating a dictonary********************
##"model": "Mustang",
  #"year": 1964
#}
#print(thisdict)


###printing dict items********
#thisdict = {
 # "brand": "Ford",
  #year": 1964
#}
#print(thisdict["brand"])


#duplicates not allowed************
#thisdict = {
 # "brand": "Ford",
  #"model": "Mustang",
  #"year": 1964,
  #"year": 2020
#}
#print(thisdict)


#length of dict******
#thisdict = {
#  "brand": "Ford",
 # "model": "Mustang",
  #"year": 1964,
  #"year": 2020
#}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#print(type(thisdict))



# accessing items in dict

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#print(x)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
#print(x)

#######key method

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

#print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

#print(x) #before the change

car["color"] = "white"

#print(x) #after the change


#   to get in dict values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

#print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

#print(x) #before the change

car["year"] = 2020

#print(x) #after the change

############items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

#print(x)

######check if the key exists************
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#if "model" in thisdict:
  #print("Yes, 'model' is one of the keys in the thisdict dictionary")

##########update the dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
#print(thisdict)
 
#       adding value

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
#print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
#print(thisdict)

###########removing items***************
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
#print(thisdict)


############for removing last item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
#print(thisdict)


############removing the item by specified key name************
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
#print(thisdict)



########clear method

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
#print(thisdict)


#########   looopsss  for printing values one by one************
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#for x in thisdict:
  #print(thisdict[x])

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#for x in thisdict.values():
 # print(x)


####for keys of dict

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#for x in thisdict.keys():
  #print(x)


#               making copy of dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
#print(mydict)

################copy with dict function

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
#print(mydict)

############   nested dictonaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#print(myfamily)


#####Creating three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
#print(myfamily)

