def mult_divide(num_1, num_2):
    return (num_1 * num_2), (num_1 / num_2)


mult, divide = mult_divide(5, 4)

print("5 * 4 =", mult)
print("5 / 4 =", divide)


def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def get_primes(max_number):
    list_of_primes = []
    for num_1 in range(2, max_number):
        if is_prime(num_1):
            list_of_primes.append(num_1)
    return list_of_primes


max_num_to_check = int(input("Search for primes up to : "))

list_of_primes = get_primes(max_num_to_check)
for prime in list_of_primes:
    print(prime)


def sum_all(*args):
    sum_1 = 0
    for i in args:
        sum_1 += i
    return sum_1


print("sum : ", sum_all(1, 2, 3, 4, 5, 9))
