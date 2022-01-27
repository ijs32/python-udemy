import os

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random txt\n more random stuff")

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed)

print(my_file.name)
print(my_file.mode)
os.rename("mydata.txt", "mystuff.txt")
# os.mkdir("mydir")
# os.chdir("mydir")
# print("Current dir :", os.getcwd())
# os.chdir("..")
# os.rmdir("mydir")

with open("mystuff.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        else:
            print("Line ", line_num)
            line = line.split()
            word_count = 0
            total_chars = 0
            for word in line:
                word_count += 1
                total_chars += len(word)
            print("Number of Words : {:.1f}".format(word_count))
            print("Avg Word Length : {:.1f}".format(total_chars / word_count))
            line_num += 1
