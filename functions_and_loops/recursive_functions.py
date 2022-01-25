from unittest import result


def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result


print(factorial(4))


def fib_nums(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        solution = fib_nums(num - 1) + fib_nums(num - 2)
        return solution


num = int(input("How many values should be found :"))
i = 1
while i < num:
    fib_value = fib_nums(i)
    print(fib_value)
    i += 1
