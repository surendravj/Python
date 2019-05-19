# program to check given year is leap or not


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
            else:
                print("not leap year")
        print("it is leap year")
    else:
        print("it is not leap year")


leap_year(2036)

# program to gcd of two numbers

def find_gcd(n1, n2):
    if n1 > n1:
        smaller = n2
    else:
        smaller = n1
    for i in range(1, smaller+1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd


print(find_gcd(30, 350))

# program to find lcm of two numbers

def find_lcm(n1, n2):
    return (n1*n2)/find_gcd(n1, n2)


print(find_lcm(72, 120))
