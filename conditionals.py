'''
> greater than
< less than
>= greater than or equal to
<= less than or equal to
== equal to
!= not equal to
pretty obvious but noting anyways
'''

# simple conditional example with input
'''
drink = input("Coke or Pepsi: ")
if drink.upper() == "COKE":
    print("here is your Coke")
elif drink.upper() == "PEPSI":
    print("here is your Pepsi")
else:
    print("We dont serve that here")
'''

num_1, operator, num_2 = input("enter calculation: ").split()

num_2 = int(num_2)
num_1 = int(num_1)

if operator == "+":
    print(num_1 + num_2)
elif operator == "-":
    print(num_1 - num_2)
elif operator == "*":
    print(num_1 * num_2)
elif operator == "/":
    print(num_1 / num_2)
else:
    print("not a valid calculation")
