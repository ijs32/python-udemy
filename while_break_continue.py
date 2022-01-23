import random
import math
'''
rand_num = random.randrange(1, 51)
i = 1
while i != rand_num:
    i += 1
print("The random number is : ", rand_num)
'''
'''
i = 1
while i <= 20:
    if (i % 2) == 0:
        i += 1
    if i == 15:
        break
    print("Odd :", i)
    i += 1
'''
height = 5
i = 0
width = 1
while i <= height:
    space = " " * (height - i)          # my weird solution
    hashtags = "#" * (width)
    print("{}{}".format(space, hashtags))
    width += 2
    i += 1
space = " " * height
print("{}#".format(space))

    #
   ###
  #####
 #######
#########