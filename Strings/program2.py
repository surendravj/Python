# Program to determine whether two strings are the anagram


def is_anagram(str1, str2):
    str1_arr = []
    str2_arr = []
    if(len(str1) != len(str2)):
        return "Not anagram"
    else:
        str1 = str1.lower()
        str2 = str2.lower()
        for i in range(0, len(str1)):
            str1_arr.append(str1[i])
            str2_arr.append(str2[i])
        if sorted(str1_arr) == sorted(str2_arr):
            return "It is anagram"
        return "It is not anagram"


print(is_anagram("foal", "loof"))


# Program to divide a string in 'N' equal parts.

def n_equal_parts(str, n):
    if(len(str) % n != 0):
        print("No possible divisions")
    else:
        length = len(str)/n
        for i in range(0, len(str)):
            if(i % length == 0):
                print("  ")
            print(str[i])


n_equal_parts("surendra", 4)


# program to find the all anagrams in array


# helper function

def is_anagram1(a, b):
    a = a.lower()
    b = b.lower()
    a_arr = []
    b_arr = []
    if(len(a) != len(b)):
        return False
    else:
        for i in range(0, len(a)):
            a_arr.append(a[i])
            b_arr.append(b[i])
        if sorted(a_arr) == sorted(b_arr):
            return True
        return False

# main_function


def match_anagram(a):
    count = 0
    no_anagrams = True
    for i in range(0, len(a)):
        for j in range(i+1, len(a)):
            if is_anagram1(a[i], a[j]):
                count += 1
                no_anagrams = False
                print(
                    f"{a[i]} and {a[j]} are {count} anagrams matchs in given array")
    if(no_anagrams):
        print("There are no anagrams match in the given array")


a = ["fool", "king", "queen", "loof", "qeneu", "surendra", "ignk"]
match_anagram(a)
