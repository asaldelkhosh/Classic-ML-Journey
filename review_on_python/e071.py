# dictionary for saving fibo numbers with none value
dictionary = {}
a1 = 1
a2 = 2
dictionary[a1] = None
dictionary[a2] = None
num = int(input('Enter number: '))
while a2 <= num:
    a2 = a1 + a2
    a1 = a2 - a1
    dictionary[a2] = None

for i in range(1, num + 1):
    char = "+" if i in dictionary else "-"
    print(char, end="")
