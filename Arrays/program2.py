# program to find max number in an array

# using buidin-function
def max_num(arr):
    return max(arr)


print(max_num([3,2,4,6]))


# using logic

def max_num2(arr):
    maxnum=0
    for i in range(0,len(arr)):
        if arr[i]>maxnum:
            maxnum=arr[i]
    return maxnum

print(max_num2([45,3,38,23]))


# program to find smallest number

# using buidin_function
def min_num(arr):
    return min(arr)

# using logical method
def min_num2(arr):
    minnum=arr[0]
    for i in range(0,len(arr)):
        if arr[i]<minnum:
            minnum=arr[i]
    return minnum

print(min_num([342,232,34]),min_num2([634,432,222]))
