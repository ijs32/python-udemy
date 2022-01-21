# def add_numbers(num_1, num_2):
#     return num_1 + num_2


# print("5 + 4 =", add_numbers(5, 4))

# original_list = [1, 2, 3, 4]


# def add_two(num):
#     return num + 2


# print(list(map(add_two, original_list)))

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
