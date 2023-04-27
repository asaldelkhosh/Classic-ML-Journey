string = input('YOUR STRING:')

list = []

# finding alpha and space in a string and add them to a list
for x in string:
    if x.isalpha() == True or x.isspace():
        list.append(x)

# joining the list together
string1 = ''.join(list)
print(string1)
