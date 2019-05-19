# program to print nth feb number


def getNthfeb(n):
    if(n == 1):
        return 0
    if(n == 2):
        return 1
    return getNthfeb(n-1)+getNthfeb(n-2)


print(getNthfeb(5))

# progrm to print feb series


def print_feb(n):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    i = 2
    while(i < n):
        n3 = n1+n2
        n1 = n2
        n2 = n3
        print(n3)
        i += 1


print_feb(5)


# program to find factorial of a number

def fact(n):
    if(n == 1):
        return 1
    return n*fact(n-1)


print(fact(5))


# program to find factorial of  a number without using recursion

def fact2(n):
    fact = 1
    while(n != 0):
        fact *= n
        n -= 1
    return fact


print(fact2(5))
