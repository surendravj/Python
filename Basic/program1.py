# program to check whether given number is even or odd


def even_odd(n):
    if n % 2 == 0:
        return f"{n} is even"
    return f"{n} is odd"


print(even_odd(7))

# program to print even and odd number in given interval


def print_even_odd(start, end):
    for i in range(start, end+1):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")


print_even_odd(1, 20)

# program to print even and odd lists separately


def print_even_odd_list(start, end):
    numbers = list(range(start, end))
    evens = [even for even in numbers if even % 2 == 0]
    odds = [odd for odd in numbers if odd % 2 != 0]
    print(f"even numbers in list are {evens}")
    print(f"odd numbers in list are {odds}")


print_even_odd_list(1, 20)
