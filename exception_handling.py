# importing a specific function from a module and assigning it an alias
from decimal import Decimal as D
import random
'''
while True:
    try:
        number = int(input("Please enter a number : "))
        break

    except ValueError:
        print("You did not enter a number")
    except:
        print("Unknown Error")

print("Thanks for entering the number", number)

number = random.randrange(1, 10)
while True:
    try:
        if number == int(input("Please enter a number 1-10: ")):
            print("Congrats you guessed the correct number,", number)
            break
        else:
            print("Sorry try again!")
    except ValueError:
        print("You didnt enter a number")
'''

# accurate floats to 28 points

sum = D(0)
sum += D("0.01111111111111111111")
sum += D("0.01111111111111111111")
print("sum = ", sum)
sum -= sum
print("sum = ", sum)
