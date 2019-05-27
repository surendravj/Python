# program to search element in an arrray
arr = [14, 464, 324, 6543, 17, 234, 564]


def search_element(arr, key):
    noElement = True
    for i in range(0, len(arr)):
        if(arr[i] == key):
            print(f"{ key } is located at indec no {i+1}")
            noElement = False
            break
    if(noElement):
        print("Match not found")


search_element(arr, 2345)


# program to find first occuring prime number in a array

# helper function to validate prime

def is_prime(n):
    count = 0
    for i in range(1, n+1):
        if(n % i == 0):
            count += 1
    if(count == 2):
        return True
    return False

# main function


def check_first_prime(arr):
    noPrime = True
    for i in range(0, len(arr)):
        if(is_prime(arr[i])):
            print(f"The first occuring prime number is {arr[i]}")
            noPrime = False
            break
    if(noPrime):
        print("No prime numbers in the given array")


check_first_prime(arr)
