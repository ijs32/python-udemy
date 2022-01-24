ian_dict = {"f_name": "Ian", "l_name": "Silber", "Address": "nothing street"}
print("My name :", ian_dict["f_name"])
ian_dict["Address"] = "south carolina"
ian_dict["Address"] = "city"
print("is there a city :", "city" in ian_dict)

for key, value in ian_dict.items():
    print(key, value)
# displays not here bc there is no m_name
print(ian_dict.get("m_name"))
ian_dict["m_name"] = "zap"
print(ian_dict.get("m_name", "Not here"))  # displays zap

for k, v in ian_dict.items():
    print(k, v)

ian_dict.clear()

# derek_dict = {"f_name": "Derek", "l_name": "Banas", "address": "123 Main St"}
# print(derek_dict["f_name"])
# derek_dict["address"] = "215 North St"
# print(derek_dict["address"])
# derek_dict["city"] = "Pittsburgh"
# print(derek_dict.get("city"))
# del derek_dict["f_name"]


# employees = []
# f_name, l_name = input("Enter employee full name : ").split()
# employees.append({"first name": f_name, "last name": l_name})
# print(employees)

# Solve the problem
# Output below -
# Enter a customer (Y/n) : y
# Enter customer name : Ian S
# Enter a customer (Y/n) : y
# Enter a customer name : Alexa W
# Enter a customer (Y/n) : n
# Ian S
# Alexa W


customers = []
while True:
    y_n = input("Enter a customer (Y/n): ")
    if y_n.lower() == "y":
        f_name, l_name = input("Enter customer name :").split()
        customers.append({"first name": f_name, "last name": l_name})
    elif y_n.lower() == "n":
        for customer in customers:
            print(customer["first name"], customer["last name"])
        break
    else:
        print("please enter a Y or N")
