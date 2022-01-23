import random
nums_list = []
for i in range(5):
    nums_list.append(random.randrange(1, 9))

sorted(nums_list)
nums_list.reverse()
nums_list.insert(5, 10)  # index first, value to add second
nums_list.remove(10)  # removes any 10s from the list
nums_list.pop(2)  # removes from index position 2

print(nums_list)

my_list = [5, 2, 9, 1]
a_list = list(range(1, 5))
print("Length :", len(my_list))
print("1st Index :", my_list[0])
print("1st 3 Values :", my_list[0:3])
print("9 in list :", 9 in my_list)
print("Index for 2 :", my_list.index(2))
my_list.remove(1)
my_list.pop(0)
my_list.insert(0, 10)
my_list = sorted(my_list)
print("Sorted :", my_list)
print("Sorted :", list(reversed(my_list)))
