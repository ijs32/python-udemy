import random
# notes
rand_list = ["string", 4.0, 24]
one_to_ten = list(range(11))
rand_list = rand_list + one_to_ten
print(rand_list[0])
print(len(rand_list))

first_3 = rand_list[0:3]
for i in first_3:
    print("{} : {}".format(first_3.index(i), i))

print(first_3[0] * 3)
print(4.0 in first_3)  # => true
print("index of string: ", first_3.index("string"))
print("{} is listed {} times".format("string", first_3.count("string")))
first_3[0] = "New string"
first_3.append("Another string")

# practice: generate a random list of n values between 1-9


def random_nums(n):
    nums = []
    for i in range(n):
        nums.append(random.randrange(1, 9))
    return nums


nums_list = random_nums(9)
i = len(nums_list) - 1
while i > 1:
    j = 0
    while j < i:
        if nums_list[j] > nums_list[j+1]:
            temp = nums_list[j]
            nums_list[j] = nums_list[j + 1]
            nums_list[j+1] = temp
        j += 1
    i -= 1
print(nums_list)
