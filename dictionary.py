dictionary = dict()
print(dictionary)
print(type(dictionary))

print("Adding elements to dictionary")
dictionary[1] = 'one'
dictionary[2] = 'Two'
dictionary[3] = 30
dictionary[4] = 'vinod'
print(dictionary)

#creating dictionary using dict() method
empty_dict = dict({'name':'vinod','age':30,'number':7569352177})
print(empty_dict)

new_dict =dict([('name','vnod'),['age',30],{'location','kollapur'},['wife','suvarna']])
print(new_dict)

("nested dictionary")

nested_dict = {'name':'vinod','age':26,'contact':{'sim1':7569352177,'sim2':6302260388},
               'address':{'H.no':[2111,294],'locations':{'present':"Bangalore",'permenent':'kollpur'}}
               }
print(nested_dict)


print("Adding elements to dictionary")
dict1 = dict()
dict1['name'] = "vinod"
dict1['age'] = 26
dict1['number'] = 123
dict1['contact'] = 6302260388,7569352177,7601003960
dict1[5] = {'address':{'h.no':2111,'pincode':508252}}
print(dict1)

print("Accessing elements form the dictionary")
mydict = {'name': 'vinod', 'age': 26, 'contact': {'sim1': 7569352177, 'sim2': 6302260388}, 'address': {'H.no': [2111, 294], 'locations': {'present': 'Bangalore', 'permenent': 'kollpur'}}}
print(mydict['name'])
print(mydict['age'])
print(mydict['contact'])
print(mydict['contact']['sim2'])
print(mydict['address'])
print(mydict['address']['locations'])
print(mydict['address']['locations']['present'])



print("accessing elements by using get()")

"""
python dictionary get() return value for given key is present.if not it return none
syntax:
dict_name.get(key,defult=None)
"""

d = {'coding': 'good', 'thinking': 'better'}
print(d.get('thinking'))
print(d.get('vinod','NotFound'))



test_dict = {'Gfg' : {'is' : 'best','am':'vinod'}}
res = test_dict.get('Gfg',{}).get('am')
print(res)
res1 = test_dict.get('Gfg',{}).get('is')
print(res1)

mydict = {'name': 'vinod', 'age': 26, 'contact': {'sim1': 7569352177, 'sim2': 6302260388}, 'address': {'H.no': [2111, 294], 'locations': {'present': 'Bangalore', 'permenent': 'kollpur'}}}
print(mydict.get('name'))
result = mydict.get('contact')
print(result)
result = mydict.get('contact',{})['sim1']
print("result:",result)

res1 = mydict.get('address',{}).get('H.no')[1]
print(res1)

result = mydict.get('address',{}).get('locations',{}).get('present')
print(result)

print("deleting element form dictionary")
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
del Dict['name']
print(Dict)
mydict = {'name': 'vinod', 'age': 26, 'contact': {'sim1': 7569352177, 'sim2': 6302260388}, 'address': {'H.no': [2111, 294], 'locations': {'present': 'Bangalore', 'permenent': 'kollpur'}}}
del mydict['contact']['sim2']
del mydict['address']['locations']['present']
del mydict['address']['H.no'][0]
print(mydict)



print("Example for copy() method")
original = {'name':'vinod','age':30,'gender':'Male','role':'developer'}
new = original.copy()
print("original dictionary:",original)
print("new dictionary:",new)

print("\n")

new['location'] = 'Bangalore'
print("original dictionary:",original)
print("new dictionary:",new)

mydict = {'name': 'vinod', 'age': 26, 'contact': {'sim1': 7569352177, 'sim2': 6302260388}, 'address': {'H.no': [2111, 294], 'locations': {'present': 'Bangalore', 'permenent': 'kollpur'}}}
print(mydict.items())
print(list(mydict.keys())[2])



import json
print("Covert string dictionary to python dictionary")
string_dict = '{"name":"vinod","age":30,"location":"kollapur"}'
print(type(string_dict))

python_dict = json.loads(string_dict)
print(python_dict)
print(type(python_dict))
"""
json.loads:
its convert jsong data into python dictionary
json.dumps:
its convert python dictionary to json data
"""

print("convert string dictionary to python dictionary using ast.literal_eval")
import ast

test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
print(type(test_string))

res = ast.literal_eval(test_string)
res1 = eval(test_string)
print(res)
print(res1)
print(type(res))




print("Example for sorting dictionary by key")
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32,'aravind':50}
keys = list(myDict.keys())
sort_keys = sorted(keys)
print(keys)
print(sort_keys)
print(sort_keys[0])

sort_dict = dict([(i,myDict[i]) for i in sort_keys])
print(sort_dict)

print("Sorting a dictionary by key")
mydict = {'pawankalayan':52,'chiranjeevi':62,'ramcharan':35,'ntr':36,'nagarjuna':63}

keys = mydict.keys()
sorted_keys = sorted(keys)
print(sorted_keys)
sort_dict = dict([(keys,mydict[keys]) for keys in sorted_keys])
print(sort_dict)

print("\n")

print("Example for sort dictionary by values")
age_dict = {'pawankalayan':52,'chiranjeevi':62,'ramcharan':35,'ntr':36,'nagarjuna':63,'samantha':30,'rathika':28}

print(list(age_dict.items()))

print(list(age_dict.items())[0])
print(list(age_dict.items())[1][0])

sort_by_age = dict(sorted(age_dict.items(), key=lambda x:x[0]))
print(sort_by_age)


keys_list = list(age_dict.keys())
sorted = sorted(keys_list)
print(sorted)

sort_dict_by_keys = dict([(key,age_dict[key]) for key in sorted ])
print(sort_dict_by_keys)















print('\n')
print('\n')
print('\n')



















