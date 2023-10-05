tpl = ()
print(type(tpl))

"""
tpl[0] = '1'
print(tpl)
Note:Tuple does not support item assignment
note2:tuple does not support item deletion
"""

print("Creating a tuple")
tpl = ('vinod',1,2,3,'P',53.69,True,'vinod')

print(type(tpl))
print(tpl)

print("accessing elements from tuples")
print(tpl[5])
print(tpl[7])


str = tuple('GEEKSFORGEEKS')
print(str)
print(str[5])


result = sorted(str)
print(result)


students = [
	{'name': 'John', 'age': 20},
	{'name': 'Alice', 'age': 18},
	{'name': 'Bob', 'age': 22}
]
for student in sorted(students,key=lambda x: x['name']):
    print(student)



tple = ('vinod',1,2,3,'P',53.69,True,'vinod')

result = tple.index('vinod')
print(result)


print("Example for enumerate() method")
"""
The enumerate() method adds counter to an iterable and it is return in the form of enumerationg objects.
the enumerating object can be used directly for loop or converted into list of tuples using list function.

syntax:
enumerate(iterable,start=0)
"""
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
obj1 = list(enumerate(l1,0))
obj2 = list(enumerate(s1))

print(obj1)
print(obj2)


print("enumerate object using for loop")
names = ('vinod','suvarna','Pawankalyan','renudesai','sunnyleoun')
for count ,name in enumerate(names,100):
	print(count,name)


names = ('vinod','suvarna','Pawankalyan','renudesai','sunnyleoun')
enum_names = enumerate(names)
print(next(enum_names))
print(next(enum_names))
print(next(enum_names))
print(next(enum_names))


print("Examples for all() method")
tpl = all((True,True,True,True,True))  #---> True
print(tpl)
tpl1 = all((True,True,False,True,True)) # ----> False
print(tpl1)
tpl2 = all(()) #---> True
print(tpl2)

lst = (2,4,6,8,12,10)
result = all((ele % 2 == 0 for ele in lst))
print(result)


sets = {}
print(all(sets))

dict = dict()
print(all(dict))


str = "2565"
print(all(str))


print("\n")


print("Examples for any()")
"""
any():any() method return True if any of element in the iterable(list,tuple,set,dictioanry,string etc) is True
else it return False
syntax:
any(iterable)
"""

list1 = [False,False,False,False,True] # ---> True
print(any(list1))
lst1 = any([])
print(lst1)

tuple1 = (False,False,False,False) #----> False
print(any(tuple1))

l = [1,0,0,False]
print(any(l))


students = [
	('vinod',30,'hyderabad',756912),
	('suvarna',26,'kollapur',63022),
	('susma',32,'nijamabad',99458),
	('ashwitha',10,'kothapet',36498)
]
print(type(students))
sort_lst = sorted(students,key=lambda x:x[0])
print(sort_lst)
sort_lst1 = sorted(students,key=lambda i:i[2])
print(sort_lst1)



student_dict = [
	{'name':'vinod','age':30,"location":'koyyalagudem'},
	{'name':'suvarna','age':30,'location':'kollapur'},
	{'name':'anirwesh','age':8,'location':'kothapet'},
	{'name':'anasuya','age':42,'location':'Hyderabad'}

]

sorted_Dict = sorted(student_dict,key=lambda x:x['location'])
print(sorted_Dict)
for student in sorted(student_dict,key=lambda x:x['location']):
	print(student)
























