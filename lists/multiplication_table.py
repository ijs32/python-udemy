# fill cells in multi dimensional multiplication table 1-9

multi_table = []
for i in range(1, 10):
    temp_list = []
    for i2 in range(1, 10):
        product = i * i2
        temp_list.append(product)
    multi_table.append(temp_list)

print(multi_table)

# better solution
multi_table = [[0] * 10 for i in range(10)]
for i in range(1, 10):
    for i2 in range(1, 10):
        multi_table[i][i2] = i * i2

print(multi_table)
