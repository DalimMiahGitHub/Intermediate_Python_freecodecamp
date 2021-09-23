# lists : ordered, mutable, allows duplicates
mylist = [5,True,"apple","apple"]

#create and empty list and fill with items later
mylist2 = list()

#loop through
for i in mylist:
    pass

#find item in list
if "apple" in mylist:
    x = True
else:
    x = False

#list methods
mylist.append("lemon")
mylist.insert(3,"blueberry")
gepoppter_eintrag = mylist.pop() #.pop() entfernt das letzt Element
print(gepoppter_eintrag)


''' weitere nützliche Methoden:
.clear() leert die Liste
.reverse() Reihenfolge umdrehen
.sort() sortiert von niedrig nach hoch
 new_list = sorted(mylist) lässt die original Liste in der ursprünglichen Reihenfolge
'''

mylist2 = [0] * 5  # erzeugt denselben Eintrag mehrfach

new_list = mylist + mylist2 # list concat über +

'''
Achtung wenn man Listen kopieren will, muss man .copy() nutzen, da sonst die Kopie auf das Original zeigt und auch das Original verändert
'''
list_copy = mylist.copy()
list_copy.append("test")
print(mylist)
# alternative für "echte" Kopie
list_copy2 = mylist[:]
print(list_copy2)

'List comprehension'
a = [1,2,3,4,5]
b = [i*i for i in a]
print(b)