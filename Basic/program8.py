# program to add invidual intergers in an integer


def sum_integers(n):
    temp = n
    sum = 0
    while(temp != 0):
        digit = int(temp % 10)
        sum += digit
        temp = int(temp/10)
    return sum


def swap(a, b):
    print(f"{a} {b}")
    a = a+b
    b = a-b
    a = a-b
    print(f"{a} {b}")


print(sum_integers(143))
swap(10, 11)
