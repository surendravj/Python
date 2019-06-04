class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pull(self):
        if(self.isEmpty()):
            return "Underflow"
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def printStack(self):
        return items


def isnum(num):
    num = int(num)
    if(num > 0 or num <= 9):
        return True
    return False


def evaluatePostFix(str):
    s = Stack()
    for c in str:
        if(c.isdigit()):
            s.push(c)
            print('true')
        else:
            val1 = s.pull()
            val2 = s.pull()
            if(val1 == "Underflow" or val2 == "Underflow"):
                return f"Invalid postfix expression"

            s.push(str(eval(val1 + c + val2)))

    return s.pull


print(evaluatePostFix("231*+9-"))
