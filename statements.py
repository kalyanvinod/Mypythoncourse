condition1 = False
if condition1:
    print("True")
else:
    print('False')
print("Outside the black")


a = 5
b = 5
if a == b:
    print('True')
    if b == a:
        print('True')
    print("True")
print("Not in IF")


print("\n")
condition_a = True
condition_b = True
if condition_a:
    print("Block 1")
    if condition_b:
        print("Block 2")
    print("Block 3")
print("Block 4")

print("\n")
condition_a = True
condition_b = False
if condition_a:
    print("Block 1")
    if condition_b:
        print("Block 2")
    print("Block 3")
print("Block 4")

print("\n")

condition_a = False
condition_b = True

if condition_a:
    print("Block 1")
    if condition_b:
        print("Block 2")
    print("Block 3")
print("Block 4")

print("\n")
condition_a = False
condition_b = False

if condition_a:
    print('Block 1')
    if condition_b:
        print("Block 2")
    print("Block 3")
print("Block 4")



print("\n")
condition_a = True
condition_b = False

if condition_a:
    print('Block 1')
else:
    if condition_b:
        print("Block 2")
    print("Block 3")
print("Block 4")


print("\n")
condition_a = False
condition_b = True

if condition_a:
    print("Block 1")
else:
    if condition_b:
        print("Block 2")
    print("Block 3")
print("Block 4")

print("\n")

condition_a = False
condition_b = False

if condition_a:
    print("Block 1")
else:
    if condition_b:
        print("Block 2")
    print("Block 3")
print("Block 4")


print("\n")
print("Print greatest number")
a = 15
b = 14
c = 17

if a > b and a > c:
    print(a)
else:
    if b > c:
        print(b)
    else:
        print(c)

print("\n")
print("Smallest number amoung three number")

if a < b and a < c:
    print(a)
else:
    if b < c:
        print(b)
    else:
        print(c)


print("\n")
condition_a = False
condition_b = False

if condition_a:
    print("Block 1")
elif condition_b:
    print("Block 2")
else:
    print("Block 3")

"""
Atm_Pin = input("Please Enter Your Pin:")
count = 3
Balance = 5000
withdrawal_amount = 
if int(len(Atm_Pin)) == 4:
    print("1 -- Cashwith drawal")
    print("2 -- Balance Enquire")

    choice = int(input("Please Select the tansaction:"))

    if choice == 1:
        W = int(input("Please Enter Amount"))
        if (W < Balance) or (W == Balance):
            print("Please Collect Your Cash")
            Balance = Balance - W
            print(Balance)
        else:
            print("Insufficent Founds")
    elif(choice == 2):
        Balance = Balance - W
        print("Your available amount is:",)









else:
    print("Invalid Pin")
"""







