# program to reverse a interger


def reverse_num(n):
    temp = n
    reversed_num = 0
    while(temp != 0):
        digit = int(temp % 10)
        reversed_num = reversed_num*10+digit
        temp = int(temp/10)
    return reversed_num


print(reverse_num(123))


# program to validate palindrom number

def is_palindrom(n):
    reversed_num = reverse_num(n)
    if(reversed_num == n):
        return True
    return False


print(is_palindrom(1212))

# program to check whether reverse of number is prime or not


def is_prime(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if(count == 2):
        return True
    return False


def check_reverse_prime(n):
    if(is_prime(reverse_num(n))):
        return True
    return False


print(check_reverse_prime(22))
