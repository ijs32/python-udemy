import os

with open("mydata.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("Some random txt")

with open("mydata.txt", encoding="utf-8") as my_file:
    print(my_file.read())

print(my_file.closed)

print(my_file.name)
print(my_file.mode)
os.rename("mydata.txt", "mystuff.txt")
os.rmdir("mydir")
os.mkdir("mydir")
os.chdir("mydir")
print("Current dir :", os.getcwd())
os.chdir("..")

with open("mystuff.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        else:
            print("Line : ", line_num, " : ", line, end="")
            line_num += 1
