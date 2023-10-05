lst = []
print(type(lst))
print("Accessing Element form the list")
mylst = ['vinod','30','suvarna','29','koyyalagudem',508252,'kollapur',['suvarna','7601003960'],['vinod','6302260388']]

print(mylst[5])
print(mylst[6])
print(mylst[7])
print(mylst[7][0])



print("Adding elements to list using append()method")
empty_lst = []
empty_lst.append('vinod')
empty_lst.append('suvarna')
empty_lst.append(30)
empty_lst.append(1)
print(empty_lst)
empty_lst.append((7,8,9))
empty_lst.append([1,2,3])
print(empty_lst)
empty_lst.append({'location':'kollapur'})
print(empty_lst)
empty_lst.append([])
print(empty_lst)


print("Adding Elements to list using insert() method")
lst = [0,2,6,8,9,4,10]
lst.insert(1,1)
print(lst)
lst.insert(3,3)
print(lst)
lst.insert(5,5)
print(lst)
lst.insert(1,('vinod','suvarna'))
print(lst)
lst.insert(2,['kollapur','koyalagudem'])
print(lst)
lst.insert(5,{'number':7569352177})
print(lst)


print("adding elements to list using exrend()method")
newlist = []
tpl = tuple(newlist)
print(tpl)
newlist.extend((7,8,9))
newlist.extend([[4,5,6]])
newlist.extend([{'name':'vinod','age':30}])
print(newlist)


print("Reversing a list using reverse() method")
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)

result = list(reversed(mylist))
print(result)

print("Remove element from the list using remove() method")
#list_name.remove(object)
lst = [0, ('vinod', 'suvarna'), ['kollapur', 'koyalagudem'],0,0, 1, 2, 3,4, 5,6,7, 8, 9, 10]
lst.remove(['kollapur', 'koyalagudem'])
lst.remove(0)
for i in range(1,10):
    lst.remove(i)
print(lst)


list1 = [1, 2, 3, 4, 2, 1, 2, 4,1, 5,1,2,1]
count = 0

while 1 in list1:
    list1.remove(1)
print(list1)

while 2 in list1:
    list1.remove(2)
print(list1)

list1 = [1, 2, 3, 4, 2, 1, 2, 4,1, 5,1,2,1]
nums = [x for x in list1 if x != 1]
print(nums)


new_list = [1,'geeks',2,3,'geeks',4,5,'geeks',7,10,'geeks']


count = new_list.count('geeks')
print(count)

while count > 0:
    new_list.remove('geeks')
    count = count - 1
print(new_list)

new_list = [1,'geeks',2,3,'geeks',4,5,'geeks',7,10,'geeks']
while 'geeks' in new_list:
    new_list.remove('geeks')
print(new_list)

for i in new_list:
    if i == 'geeks':
        new_list.remove(i)
print(new_list)



print("Removing element from the list using pop()method")
List = [1, 2, 3, 4, 5]
print(List.pop())
print(List.pop(0))


print("List slicing")

List = ['G', 'E', 'E', 'K', 'S', 'F','O', 'R', 'G', 'E', 'E', 'K', 'S']
print(List[5:12]) #--->FORGEEK
print(List[0:5])  #--->GEEKS
print(List[3:])
print(List[:])
print(List[:10])


print("Negative index list slicing")
List = ['G', 'E', 'E', 'K', 'S', 'F','O', 'R', 'G', 'E', 'E', 'K', 'S']
print(List[-1])
print(List[-5:-1])
print(List[-8:])
print(List[:-8])


print("List Comprehensions")
"""
newlist = [expression(element) for element in oldlist if condition]

"""

list = [2,5,9,7,3,10,14]
square_list = [x * x for x in list if x % 2 == 0]
print(square_list)

square_list =[]
for i in list:
    if i % 2 == 0:
        square_list.append(i**2)
print(square_list)


"""
[expression(element) for element in oldlist if(conditions)]
"""


print(2**2)
print(2**3)
print(6**2)
print(6**3)

odd_square = [x ** 2 for x in range(1,11) if x % 2 == 1]
print(odd_square)

odd_square = []
for x in range(1,11):
    if x % 2 == 1:
        odd_square.append(x ** 2)
print(odd_square)


nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]
nums = [(x,y) for x in nums1 for y in nums2]
print(nums)

numslist = []
for x in nums1:
    for y in nums2:
        numslist.append((x,y))
print(numslist)

print("List Comprehensions wth multiple if condtions")

nums = [x for x in range(1,21) if x%2 == 0 if x % 5 == 0]
print(nums)

new_nums = []
for x in range(1,21):
    if x % 2 == 0 and x % 5 == 0:
        new_nums.append(x)
print(new_nums)


print("List comprehension with if-else conditions")
lst = ['Even' if i %2==0 else "odd" for i in range(1,10)]
print(lst)


age_lst = [18,10,28,32,5]
age = [str(age) +'  = Eligible' if age > 18 else "Not eligible" for age in age_lst ]
print(age)

print("Remove duplicate item from list")
mylist=[5,10,15,20,3,15,25,20,30,10,100]
new_list = []
for num in mylist:
    if num not in new_list:
        new_list.append(num)
print(new_list)

unique_list = []
new_list = [unique_list.append(num) for num in mylist if num not in unique_list]
print(unique_list)


"""
count_name = input("Enter name here:")
names=['Deepak','Reema','John','Deepak','Munna','Reema','Deepak','Amit','John','Reema']
count = names.count(count_name)
print(count)
"""



nums = [x ** 2  if x%2==0 else x*2 for x in range(1,21)]
print(nums)

lower_case = [x.lower() for x in ['A','B','C',"D"]]
print(lower_case)

text = "this is vinod from bangalore"
split = text.split()
capital = [x.capitalize() for x in split]
upper = [x.upper() for x in split]
print(capital)
print(upper)



print("Examples for sort()method")

"""
sort function is used to sort a list in both asecnding and desending order.it can be used to sort list of
integers.floting numbers,strings.

syntax:
list_name.sort(key=,reverse=)
key = function as serve as key
reverse = if reverse  is True the sorted list in desending order.
"""

lst = [2,4,5,32,6,255,5,42]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)


print("Sorting list in ascending order")
lst1 = [25,14,19,36,27,45,10,65,11,31,8]
lst1.sort()
print(lst1)

decimals = [5.012,2.59,15.204,7.89,9.45,25.147,3.954]
decimals.sort()
print(decimals)
#[2.59,3.954,5.012,7.89,9.45,15.204,25.147]

names = ['vinod','suvarna','Suvarna','nagaraju','Nandini','Poojitha','aradya','Anasuya','Bhanu','bavani']
names.sort()
print(names)


print("Sorting list in descending order")
lst1.sort(reverse=True)
print(lst1)

decimals.sort(reverse=True)
print(decimals)

names.sort(reverse=True)
print(names)


print("sort with custom function using key")



print("sort a list using sorted() method")
"""

sorted method return sorted list.it is not only for list it can acceptable any iterable.
syntax:
sorted(iterable,key=,reverse = True|False)

iterable = list,tuple,string, or collections ,dictionary,set,frozenset.
"""

numlist = [9,3,7,2,1,6,4,10,5,8]
ascending = sorted(numlist)
descending = sorted(numlist,reverse=True)
print(ascending)
print(descending)

tuple = (9,3,7,2,1,6,4,10,5,8)
tpl = sorted(tuple)
tpl1 = sorted(tuple,reverse=True)
print(tpl)
print(tpl1)

string = "python developer"
ascen = sorted(string.split())
print(ascen)

text = "LearnPython.com is awesome to learn about custom sort functions in Python"
sort_text = sorted(text.split(),reverse=True)
print(sort_text)


pokemon = [
    ('Charmander', 'Fire', 52),
    ('Blastoise', 'Water', 83),
    ('Beedrill', 'Poison', 90),
    ('Batsman','Sports',68)
]

print(type(pokemon))

lst_sort = sorted(pokemon)
print(lst_sort)
lst_sort = sorted(pokemon,reverse=True)
print(lst_sort)
print("\n")

data = [
    ('Charmander', 'Fire', 52,'apple'),
    ('Blastoise', 'Water', 83,'orange'),
    ('Vinod','Xpple',30,'banana'),
    ('Beedrill', 'Poison', 90,'guava'),
 ]

sort_data = sorted(data ,key=lambda x:x[3],reverse=True)
print(sort_data)

print("Example for sorted() method")

string = "Python sorted() function returns a sorted list. It is not only defined for the list, it accepts any iterable."
sort_str = sorted(string.split())
print(sort_str)
sort_str = sorted(string.split(),reverse=True)
print(sort_str)

print("Exmaples for list reverse() method")

"""
python reverse() is built-in function it reverse only list element.it return reversing list
syntax:
list_name.reverse()
"""
#list_name.reverse()
list1 = [1, 2, 3, 4, 1, 2, 6]
list1.reverse()
print(list1)

list2 = ['c','A','B','d','e','z','f','a']
list2.reverse()
print(list2)

tple = ['c','A','B','d','e','z','f','a']
tple.reverse()
print(tple)
"""
string = "pythondeveloper"
string.reverse()
print(string)
"""



























































