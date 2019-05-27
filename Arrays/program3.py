# program to find second largest number in the array

arr=[34,213,45,213,63]

def find_max(arr):
    max = 0
    index = None
    for i in range(0, len(arr)):
        if(max < arr[i]):
            index = i
            max = arr[i]
    return index

# print(find_max(arr))


def second_max(arr):
    arr.pop(find_max(arr))
    new_arr = arr
    second_largest = find_max(new_arr)
    return arr[second_largest]


print(second_max(arr))


# program to find second smallest element in an array


def find_min(arr):
    index = 0
    min = arr[0]
    for i in range(0, len(arr)):
        if(min > arr[i]):
            index = i
            min = arr[i]
    return index



def second_min(arr):
    arr.pop(find_min(arr))
    new_arr=arr
    second_smallest=find_min(new_arr)
    return arr[second_smallest]


print(second_min(arr))