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

# simple calculator
# num_1, operator, num_2 = input("enter calculation: ").split()

# num_2 = int(num_2)
# num_1 = int(num_1)

# if operator == "+":
#     print(num_1 + num_2)
# elif operator == "-":
#     print(num_1 - num_2)
# elif operator == "*":
#     print(num_1 * num_2)
# elif operator == "/":
#     print(num_1 / num_2)
# else:
#     print("not a valid calculation")
'''
age = int(input("What is your age: "))
can_vote = True if age >= 18 else False  # single line conditional logic
print("You can vote :", can_vote)
'''

age = 3
if age < 5:
    print("Too Young for School")
elif age == 5:
    print("Go to kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to Grade ", grade)
else:
    print("Go to College")
