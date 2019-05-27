# program to print elements in the array in the reverse order

arr = list(range(1, 6))


def reverse_print(arr):
    for i in reversed(arr):
        print(i)


# reverse_print(arr)


# program to merge two array
arr2 = list(range(6, 11))


def mergearrays(arr1, arr2):
    resultant_array = arr1+arr2
    print(resultant_array)

# program to find the repeated elements in the array


rarr = [3, 2, 6, 3, 4, 2, 4, 5, 2, 6, 3, 6, 7, 2, 4, 1, 7]


def find_repeated_elements(arr):
    repeated_array = []  # array to store repeated elements
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i] == arr[j]):
                repeated_array.append(arr[i])
                break
    repeated_array = list(set(repeated_array))
    return repeated_array


print(find_repeated_elements(rarr))


# program to find the frequency of elements in an array

# helper function to find existing number

def check_frequency(arr, i):
    if i in arr:
        return True
    return False

# main function


def frequency_count(arr):
    check_array = []
    for i in range(0, len(arr)):
        count = 1
        if(not check_frequency(check_array, arr[i])):
            for j in range(i+1, len(arr)):
                if(arr[i] == arr[j]):
                    count += 1
                    check_array.append(arr[i])
            print(f"{arr[i]} ||  {count}")


frequency_count(rarr)
