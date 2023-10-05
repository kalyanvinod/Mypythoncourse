"""
In Python set is unordered collection of elements mutable and duplicates are not allowed.

"""

myset = set()
print(type(myset))

string = set("GEEKSFORGEEKS")
print(string)

myset = {'geeks','for','geeks','Geeks'}
print(myset)


myset = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print(myset)



print("Adding element to a set")

"""
Elements can be added to set using built-in add() function.only one element can be added to the set.
Note:
lists cannot be added using add()method becuse lists are not hashable.tupels can be added tuples are 
immutable and hashable.
"""
emptyset = set()
emptyset.add(5)
emptyset.add(5.9)
emptyset.add(True)
emptyset.add('Suvarna')
emptyset.add('V')
print(emptyset)

"""
list cannot be added becuse list are not hashable.
emptyset.add([7,8,9])
print(emptyset)
"""
emptyset.add((4,56,23))
print(emptyset)



print("Update method in sets")
"""
For addition of two or more elements use update() method.in this case update method
accepts all list tuples string,and other sets.all this case avoid duplicates
"""

empty_set = set()
empty_set.update((1,2,3))
empty_set.update([4,5,6])
empty_set.update(('vinod'))
empty_set.update((1,9,3))
empty_set.update({'s','u'})
print(empty_set)




print("Accessing  a set element")
"""
set items cannot be accessed  becuse set are unoredered set items has no index.we can access set
using loops.
"""

my_set = set((1,2,3,4))
print(my_set)
for i in my_set:
    print(i)


print("Removeing element from the set")
"""
Remove element from the set using built in function remove.it raises error
if the element is not exist .To remove element for set without error use discard()

"""
set1 = {1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12}

set1.remove(5)
set1.remove(10)
print(set1)
set1.discard(11)
set1.discard(9)
print(set1)


print("Remove element using pop method")
"""
pop() function can also use to remove element. by defualt it removes last element.
actually sets are unordered no such way to determine wich element is to poped by pop() function..
"""
set2 = {'vinod',True,5.6,7.9,'Py',3,1}
print(set2.pop())
print(set2.pop())
print(set2.pop())
print(set2)



print("Examples for frozenset() method")
"""
Frozen sets in python are immutable objects only support for methods and opetaros that produces result without
affecting the sets or frozensets.elements of sets can be modified anytime frozensets remain same ofter creation
"""

String = set(['G', 'e', 'e', 'k', 's', 'F', 'o', 'r'])
fset = frozenset(String)
print(fset)
print(String)


str = {'G', 'e', 'e', 'k', 's', 'F', 'o', 'r'}
str.clear()
print(str)

print("Example for deepcopy")
original = {'g', 'e', 'e', 'k', 's'}
new = original.copy()

print("original set: ",original)
print("New :",new)

new.add('XXX')

print("original:",original)
print("new: ",new)


print("difference() method")
setA = {10,50,40,80,60,70}
setB = {100,15,45,60,70,40}
print(setA.difference(setB))
print(setB.difference(setA))

print("Example for difference_update()")
A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}

setA.difference_update(setB)
print(setA)





