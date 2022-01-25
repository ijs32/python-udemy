# def add_numbers(num_1, num_2):
#     return num_1 + num_2


# print("5 + 4 =", add_numbers(5, 4))

# original_list = [1, 2, 3, 4]


# def add_two(num):
#     return num + 2


# print(list(map(add_two, original_list)))

from typing import final


words = ["hello", "world", "goodbye", "no", "ok"]


def get_length(word):
    return len(word)


print(list(map(get_length, words)))

nums = [1, 2, 3]


def divide_by_two(num):
    return num / 2.0


print(list(map(divide_by_two, nums)))


def first_char(word):
    return word[0]


print(list(map(first_char, words)))


def to_string(num):
    return str(num)


print(list(map(to_string, nums)))


def is_even(num):
    if num % 2 == 0:
        return num
    else:
        return "Not even"


print(list(map(is_even, nums)))


def shorter_than_four(word):
    if len(word) < 4:
        return word


print(list(map(shorter_than_four, words)))


def change_name():
    global gbl_name
    gbl_name = 'Sammy'


# use global variables if you want to affect something outside a function
gbl_name = "Charles"
change_name()
print(gbl_name)


def get_sum(num_1, num_2):
    return num_1 + num_2   # values must be returned


print(get_sum(5, 4))


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


pi = "3.14"
print("is pi a float : ", is_float(pi))


# def solve_eq(string):
#     eq = string.split()
#     numbers = []
#     for i in eq:
#         try:
#             int(i)
#             numbers.append(int(i))   # my less pro answer
#         except:
#             continue
#     return("x = {}".format(numbers[-1] - numbers[0]))


# print(solve_eq("x + 4 = 9"))

def solve_eq(string):
    x, operator, num_1, equal, num_2 = string.split()
    num_1, num_2 = int(num_1), int(num_2)     # much better solution
    return("x = {}".format(num_2 - num_1))


print(solve_eq("x + 4 = 9"))
