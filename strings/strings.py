# print(type(3))
# print(type(3.1))
# print(type("3.1"))

sample_string = "lorem ipsum dolor"

print("length: ", len(sample_string))

print(sample_string[0])
print(sample_string[10])
print(sample_string[0:6])
print(sample_string[6:])
print("every other", sample_string[0:-1:2])
print("reverse string", sample_string[::-1])
print("Green" + "eggs")
print("Green" * 5)
num_string = str(4)

for char in sample_string:
    print(char)

for i in range(0, len(sample_string)-1, 2):
    print(sample_string[i] + sample_string[i + 1])

'''
Unicode characters
A - Z = 65 - 90
a - z = 97 - 122
'''

# print("A =", ord("A"))
# print("65 =", chr(65))

# convert an uppercase string into unicode and then from unicode back to the original

string = input("Enter a word : ")
unicode_string = ""
translation = ""
for char in string:
    unicode_string += str(ord(char) - 23)
print("secret message =", unicode_string)
for i in range(0, len(unicode_string)-1, 2):
    char = int(unicode_string[i] + unicode_string[i + 1])
    char = chr(char + 23)
    translation += char
print("uncovered word =", translation)
