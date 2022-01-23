rand_string = "       important information      "
rand_string = rand_string.lstrip()
rand_string = rand_string.rstrip()  # or just use .strip for both sides
rand_string = rand_string.upper()
rand_string = rand_string.lower()
print(rand_string)

rand_string = "this is an important string"
list = ["bunch", "of", "words"]
print(" ".join(list))
print(rand_string.replace(" an", " a kind of"))

######################################################
#############     Acronym generator    ###############
######################################################

string = input("enter some words : ").split()
acronym = ""
for word in string:
    acronym += word[0].upper()

print("your acronym is :", acronym)

######################################################
#############     More methods wooo    ###############
######################################################

z = "z"
print("Is z a letter :", z.isalpha())
print("Is z a letter :", z.isdigit())
print("Is z a letter :", z.islower())
print("Is z a letter :", z.isupper())
print("Is z a letter :", z.isspace())
