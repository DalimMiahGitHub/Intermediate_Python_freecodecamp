# dictionaries: unordered, mutable
mydict = {"name":"Max","age":"28","city":"New York"}
mydict2 = dict(name="Mary",age=27) # with dict() no quotes are needed for keys
value = mydict["name"]

#add new element to dict
mydict["email"]="Max@Max.com"

#element entfernen
#mydict.popitem()

#key finden
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["lastname"])
except:
    print("Error")

#loop through dict
for key in mydict:
    print(key)
for value in mydict.values():
    print(value)
for key,value in mydict.items():
    print(key,value)

#copy a dict
mydict_copy = mydict #will cause modification of the original
mydict_copy = mydict.copy() #will create an actual copy and leave original as is

#merge 2 dicts
mydict.update(mydict2)
print(mydict)