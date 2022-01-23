from audioop import mul
import math
even_list = [i*2 for i in range(10)]  # creates a list of evens
for k in even_list:
    print(k, end=", ")

multi_list = [[0] * 10 for i in range(10)]
multi_list[0][1] = 10
print(multi_list[0][1])
for i in range(10):
    for j in range(10):
        multi_list[i][j] = "{} : {}".format(i, j)

for i in range(10):
    for j in range(10):
        print(multi_list[i][j], end=" || ")


