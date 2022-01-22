for i in [2, 3, 4, 5, 6, 7, 9]:
    print("i = ", i)
for i in range(5):
    print("i = ", i)

for i in range(21):
    if i % 2 != 0:          # simple problem to find odd numbers in a range
        print("{} is an odd number".format(i))


your_float = input("enter a float pls : ")
your_float = float(your_float)
print("rounded to 2 decimals : {:.2f}".format(your_float))


# simple investment interest calculator
investment, interest = input(
    "enter your investment and expected interest : ").split()
investment = int(investment)
interest = int(interest)
for i in range(11):
    investment += (investment * (interest * 0.01))
print("Your invested amount after 10 years equals {:.2f}".format(investment))

# for i in range(1, 21):
#     print(i)
