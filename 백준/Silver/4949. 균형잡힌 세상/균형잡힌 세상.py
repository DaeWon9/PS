import sys
from collections import deque

def check_bracket(str):
    leftBracketCount = 0
    stack = deque()
    for char in str:
        if (char == '(' or char == '['):
            stack.append(char)
            leftBracketCount += 1
        elif (char == ')'):
            if (len(stack) == 0):
                return False
            leftBracketCount -= 1
            if (stack.pop() != '('):
                return False
        elif (char == ']'):
            if (len(stack) == 0):
                return False
            leftBracketCount -= 1
            if (stack.pop() != '['):
                return False
    if (leftBracketCount == 0):
        return True
    return False

while (True):
    input_string = sys.stdin.readline()
    if (len(input_string) == 2 and input_string[0] == '.'):
        break

    if (check_bracket(input_string)):
        print("yes")
    else:
        print("no")