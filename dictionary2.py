names_dict = {'sharif':45,'vinod':30,'amrutha':64,'balaji':42,'chaitra':72,'damodar':55}

all_keys = list(names_dict.keys())
print(all_keys)
sort_allkeys = sorted(all_keys)
print(sort_allkeys)

sort_dict_by_keys = dict([(keys,names_dict[keys]) for keys in sort_allkeys])
print(sort_dict_by_keys)

values = list(sorted(names_dict.values()))
print(values)
sort_by_values = dict(sorted(names_dict.items(), key=lambda x:x[1]))
print(sort_by_values)




print("Example for dicitionary comprehensions")
"""
syntax:
{key:value for (key:value) in old_dict.items() if (conditions)}
"""
mydict = {1:1,2:2,3:3,4:4,5:5}
square_dict = {k:v**2 for k,v in mydict.items()}
print(square_dict)


names_dict = {'name':'vinod',30:'age','location':'Bangalore','role':'developer'}
new_dict = {key:value.upper() for key,value in names_dict.items()}
print(new_dict)


old_price = {'milk':25,'bread':45,'eggs':150,'chicken':200,'ricebag':1500}
new_price = {item:price*2 for item,price in old_price.items() if price >= 50}
print(new_price)


original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 17}
even_dict = {name:age for (name,age) in original_dict.items() if age>=40 if len(name) >= 5}
print(even_dict)


age_dict = {name:("Not eligible" if age <=18 else "eligible") for (name,age) in original_dict.items()}
print(age_dict)


nums_dict ={'maths':75,'telugu':95,'Hindi':32,'social':86,'sceince':89}

result = {subject:("Passed" if marks >= 35 else "Failed") for (subject,marks) in nums_dict.items()}
print(result)


"""
Ternary operator:
In python ternary operator determaine if condition is true or false then return approximate value.
syntax:
[on_true] if [condition] else [on_false]

"""
lst = [4,8,7,3,5,9]
even_num = ["Even" if value % 2 ==0 else "Odd" for value in lst]
print(even_num)


print("Examples for Membership operators")




def overlapping(list1,list2):
    l1 = 0
    l2 = 0
    for i in list1:
        l1 +=1
    for j in list2:
        l2 += 1
    for i in range(0,l1):
        for j in range(0,l2):
            if (list1[i] == list2[j]):
                return 1
    return 0



list1 = [1, 2, 3, 4, 5]
list2 = [6, 7,2, 8, 9]
if(overlapping(list1,list2)):
    print("overlapping")
else:
    print("Not overlapping")









