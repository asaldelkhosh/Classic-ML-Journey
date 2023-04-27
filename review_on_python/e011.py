# define a function to check if a number is prime or not
def isPrime(num):
    primeFlag = True
    n = 2
    if num == 1:
        primeFlag = False
    while num**(1/2) >= n:
        if num % n == 0:
            primeFlag = False
            break
        n +=1
    return primeFlag

if __name__ == "__main__":
    num = int(input("Enter number: "))
    print("\n[ ",isPrime(num),' ]\n')