print("Example for reversed()")
"""
syntax:
sorted(iterator)
"""
lst1 = ['c','A','B','d','e','z','f','a']
rev_lst = list(reversed(lst1))
print(rev_lst)



tuples = ('c','A','B','d','e','z','f','a')
rev_tpl = tuple(reversed(tuples))
print(rev_tpl)

string = "pythondeveloper"
str_rev = list(reversed(string))
print(str_rev)


print("Example for count() method")
"""
count():it return number of times given object occure in given list
syntax:
list_name.count("obj")
"""

def myfunc(text):
    return text.count('a')
text = "This banana i like bananaa"
print(myfunc(text))

mylist = [4,5,7,6,5,2,10,5,9,4,3,5,5,5]
total = mylist.count(5)
print(total)

tpl = (4,5,7,6,5,2,4,4,4,10,5,9,4,3,5,5,5)
total = tpl.count(4)
print(total)

string = "python developer"
chars = string.count('e')
print(chars)

tpl = (4,5,7,6,5,2,4,4,4,10,5,9,4,3,5,5,5,7)
res = [(l,tpl.count(l)) for l in set(tpl)]
print(res)
dictionary = [dict((l,tpl.count(l)) for l in tpl)]
print(dictionary)


print("Example for index() method")
"""
Python index() method is built in function python wich can be searches for given substring from
start of list and return first occurrence.
list_name.index(object,start,end)
"""


print("Example for max() method")
"""
Python max() function return largest one in an iterable 
"""

max1 = lambda a,b,c ,d:max(a,b,c,d)
print(max1(5,6,10,7))

list1 = [7,15,10,6,9,3,0]
print(max(list1))

var = 'ap'
var1 = 'vinod'
var2 ='suvarna'
var3 = 'money'
result = max(var,var1,var2,var3,key=len)
print(result)



print("Examples for any()")
"""
any() method is buildin function python it return true any of its True.it return False
if empty or all are false.
all()method is built in function it return true if all elements true or empty sequence
"""

print(any(['False','True','False','False','Flase']))
print(any([False,False,False,False]))
print(any(([False,False,True,False])))
print(any([]))

print("\n")

print("Examples for all() method")
print(all([True,True,True,True])) #---> True
print(all([True,True,True,True,False])) #---->False
print(all([False,False,False,False,False]))  #--->False
print(all([]))

print("Example for ord() method")
"""
This method return unicode from the given charecter
"""
print(ord("A"))
print(ord('a'))
print(ord('v'))


print(ord('S'))
print(chr(83))

print(chr(65))










