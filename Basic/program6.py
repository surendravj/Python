# program to check given number is prime or not
def is_prime(n):
    count = 0
    start = 1
    while(start <= n):
        if(n % start == 0):
            count += 1
        start += 1
    if(count == 2):
        return True
    return False


print(is_prime(11))


# program to print prime numbers in given interval

def print_prime(start, end):
    for i in range(start, end+1):
        if(is_prime(i)):
            print(i)


print_prime(1, 10)
