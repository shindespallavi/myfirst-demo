myDict = {
    "fast":"In a Quick Manner",
    "pallavi":"A Coder" ,
    "marks":[1,2,5],
    "anotherDict":{'rockstar':'angel'},
    1:2
    }

# dictonary methods
print(type(myDict.keys()))# prints the keys of dict
print(myDict.values()) # prints the key values of dict
print(myDict.items()) # print the (key,value)for all contents of the dict
print(myDict)
updateDict = {
    "Lovish":"Friend",
    "Niranajan":"Friend",
"pallavi":"A gamer"

}

myDict.update(updateDict) # updates the dict by adding key_values pairs from updateDict
print(myDict)
print(myDict.get("pallavi"))# prints value associated with key "pallavi"
print(myDict("pallavi")) # prints value associated with key "pallavi"

# diff between .getand[] syntax dictonary
print(myDict.get("pallavi2"))# returns none as pallavi2 is not present in the dict
print(myDict("pallavi2")) # throws an error as pallavi2 is not present in the dict
