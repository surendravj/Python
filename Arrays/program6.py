# program to find the median of an array

# helper function to merge two arrays


def merge_arrays(arr1, arr2):
    arr3 = arr1+arr2
    return sorted(arr3)


arr1 = [5, 4, 3, 2, 1]
arr2 = [11, 10, 9, 8, 7]


def find_median(arr1, arr2):
    arr3 = merge_arrays(arr1, arr2)

    array_len = len(arr3)-1

    array_mid = int(array_len/2)

    median = arr3[array_mid]+arr3[array_mid+1]

    return int(median/2)


# print(find_median(arr1, arr2))


# program to rotate array elements towards left


def rotateLeft(arr):
    i = 0
    j = len(arr)-1
    while(i != j):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        i += 1
        j -= 1
    return arr


arr = [45, 34, 56, 23, 64]
print(rotateLeft(arr))


# program to move elements fowards left on given range


# helper function to move elements one by one
def move_elements(arr):
    j = len(arr)-1
    temp = arr[0]
    i = 0
    while(i != j):
        arr[i] = arr[i+1]
        i += 1
    arr[j] = temp


def loop_Elements(arr, index_Limit):
    if len(arr)-1 > index_Limit:
        for i in range(0, index_Limit+1):
            move_elements(arr)
        return arr
    return "Limit Overflow"


arr3 = [5, 4, 3, 2, 1]
print(loop_Elements(arr3, 10))


# program to print the elements that are matched with the index of that element


def match_index_print(arr):
    no_index_match = True
    for i in range(0, len(arr)):
        if(i == arr[i]):
            print(arr[i])
            no_index_match = False
    if(no_index_match):
        print("No match index found")


match_index_print([2, 5, 9, 5, 7, 9])  # case 1

match_index_print([2, 5, 2, 5, 4, 9])  # case 2
