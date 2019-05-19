# program to check given aphabet is valid or not


def valid_alphabet(c):
    c = str(c)
    c = c.lower()
    if(c >= 'a' and c <= 'z'):
        return (f"{c} is alphabet", True)
    return (f"{c} is not aplhabet", False)


# print(valid_alphabet(53))


def check_ovwels(c):
    c = str(c)
    c = c.lower()
    if(c >= 'a' and c <= 'z'):
        if c in 'aeiou':
            return f"{c} is ovwel"
        return f"{c} is cosnonent"
    return f"{c} is not aplhabet to check"


print(check_ovwels('u'))
