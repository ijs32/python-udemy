import random
nums_list = []
for i in range(5):
    nums_list.append(random.randrange(1, 9))

nums_list.sort()
nums_list.reverse()
# first value is the index second value is what you are inserting
nums_list.insert(5, 10)
nums_list.remove(10)  # removes any 10s from the list
nums_list.pop(2)  # removes from index position 2

print(nums_list)
