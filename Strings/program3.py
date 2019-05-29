# program to remove all white spaces in a  given string


def remove_spaces(str):
    str = str.replace(" ", "")
    return str


print(remove_spaces("my name is surendra"))


# / Program to replace lower-case characters with upper-case and vice versa.


def lower_upper_case(str):
    new_str = ""
    for i in str:
        if i >= "a" and i <= "z":
            i = i.upper()
            new_str += i
        elif i >= "A" and i <= "Z":
            i = i.lower()
            new_str += i
    return new_str


print(lower_upper_case("SUrendRa"))


# Program to replace the spaces of a string with a specific character

def replace_space(str, re_char):
    replaced_str = ""
    for i in range(0, len(str)):
        if(str[i] == " "):
            replaced_str += re_char
        elif(str[i] != " "):
            replaced_str += str[i]
    return replaced_str


print(replace_space("my name is surendra", "$"))


# program to count the occurance of a specific charcter in a string


def count_char(str, char):
    count = 0
    for i in range(0, len(str)):
        if(str[i] == char):
            count += 1
    return count


print(count_char("my name is surendra", 's'))
