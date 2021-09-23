import sys
import timeit

mytuple = ("Max",23,"Boston")
alternatives_tuple = "auch","ein","Tuple",123
print(type(alternatives_tuple))

'''
Tuple: ordered, immutable (this is the difference to list) , allows duplicates
da tuples immutable sind, sind sie teilweise effizienter als listen
'''
mylist = ["Max",23,"Boston"]
print(sys.getsizeof(mytuple),"bytes")
print(sys.getsizeof(mylist),"bytes")

print(timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)) # 1mio mal wird das statement Liste mit 5 Einträgen ausgeführt
print(timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)) # 1mio mal wird das statement Tuple mit 5 Einträgen ausgeführt

# list to tuple & tuple to list
tuple_from_list = tuple(["Max",28,"Boston"])
list_from_tuple = list(alternatives_tuple)

item = mytuple[0]
print(item)

letter_tuple = "a","p","p","l","e"
print(letter_tuple.count("p"))
print("index of l is",letter_tuple.index("l"))

'''
unpacking = mehrere Variablen in einer Zeile mit Werten aus dem Tuple belegen
unpacking klappt nur, wenn die Anzahl der Variablen = Anzahl der Elemente im Tuple
'''
name, alter, stadt = mytuple
print(name, alter, stadt)

'''
compare list and tuples
'''
