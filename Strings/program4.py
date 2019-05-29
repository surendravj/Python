# program to get all the numerical set in a string


# helper_function

def is_alpha(a):
    a = a.lower()
    if a >= 'a' and a <= "z":
        return True
    return False


def get_numerical_set(str):
    str = str.replace(" ", "")
    numerical_num = ""
    for i in range(0, len(str)):
        if not is_alpha(str[i]):
            numerical_num += str[i]
    return int(numerical_num)


print(get_numerical_set("i am 3846surendra 14 years36472 old "))


# program to count total number of words in a string

def count_strings(str):
    count = 0
    str2 = str.split(" ")
    return len(str2)


print(count_strings("i am surendra i am coding"))


# program to check given string is palindrom or not


def is_palindrom(str):
    temp = str[::-1]
    if(str == temp):
        return "palindrom"
    return "not palindrom"


print(is_palindrom("kayak"))
