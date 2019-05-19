# program to check given number is armstrong or not


def is_armstrong(n):
    temp = n
    order = len(str(n))
    n = int(n)
    sum = 0
    while(temp != 0):
        digit = int(temp % 10)
        sum += digit**order
        temp = int(temp/10)
    if(sum == n):
        return True
    return False

# program to print armstrong number in a given range

def print_armstrong(start, end):
    for i in range(start, end+1):
        if(is_armstrong(i)):
            print(i)
print_armstrong(1,160)