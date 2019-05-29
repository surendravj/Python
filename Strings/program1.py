# Program to count the total number of punctuation characters exists in a string.


def count_punc(str):
    count = 0
    for i in str:
        if i in ".,/!?;:-":
            count += 1
    return count


print(count_punc("hi! r u surendra ? yes i am ."))


# // program to count number of ovwels and consonents in a string


def count_ovwels_consonents(str):
    ovwels = 0
    consonents = 0
    str = str.lower()
    for i in str:
        if i in "aeiou":
            ovwels += 1
        elif i >= "a" and i <= "z":
            consonents += 1
    return (f"ovwels-{ovwels}  ||   consonents--{consonents}")


print(count_ovwels_consonents("surendra"))


# program to convert every ovwel into uppercase in a string


def ovwel_upperCase(str):
    converted_str = ""
    for i in str:
        if i in "aeiou":
            i = i.upper()
            converted_str += i
        elif i not in "aeiou":
            converted_str += i
    return converted_str


print(ovwel_upperCase("surendra"))
