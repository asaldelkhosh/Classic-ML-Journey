# useing the function from isPrime:
from  isPrime import isPrime

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

list = []

# finding prime numbers between two numders:
for x in range(num1,num2):
    if isPrime(x) == True:
        # adding prime numbers to a list
        list.append(x)
print(len(list))        
