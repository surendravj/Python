# program to find sum of integers in an array

arr = list(range(1, 10))

# arr=[1,2,3,4,5,6,7,8,9]

def sum_array(arr):
    total = 0
    for i in range(0,len(arr)):
        total += arr[i]
    return total


print(sum_array(arr))


#program to print multiples of n 


def n_mul(arr,n):
    no_mul=True
    for i in range(0,len(arr)):
        if(n%arr[i]==0):
            print(arr[i])
            no_mul=False
    if(no_mul):
        print("No multiples found")

n_mul(arr,13)



# program to find pair sum of n in an array 

# n=12
# 8+4=True
# 12=True


def no_pair_sumFound(arr,n):
    for i in range(0,len(arr)):
        if(arr[i]==n):
            return True
    return False


def pair_sum(arr,n):
    if(no_pair_sumFound(arr,n)):
        return True
    else:
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                if(arr[i]+arr[j]==n):
                    return True
    return False


print(pair_sum(arr,12))