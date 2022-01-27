# sort of like a list but immutable

my_tuple = (0, 1, 2, 3, 4, 5)
print("1st Value :", my_tuple[0])
print(my_tuple[0:3])
print("Length : ", len(my_tuple))
more_nums = my_tuple + (12, 123, 2)
print("12 in more_nums :", 24 in more_nums)
for i in more_nums:
    print(i)

a_list = [1, 2, 543, 23]
a_tuple = tuple(a_list)
a_list = list(a_tuple)
print("Max : ", max(a_tuple))
print("Min : ", min(a_tuple))
