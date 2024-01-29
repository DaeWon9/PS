import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def is_pop(top_operator, current_operator):
    if (priority_dict[current_operator] > priority_dict[top_operator]):
        return False
    return True

def process_operator(target_operator):
    if (target_operator == '('):
        stack.append(target_operator)
        return
    
    if (target_operator == ')'):
        while(True):
            pop_operator = stack.pop()
            if (pop_operator == '('):
                return
            print(pop_operator, end='')

    while(stack and is_pop(stack[-1], target_operator)):
        print(stack.pop(), end='')

    stack.append(target_operator)

priority_dict = defaultdict(int)
priority_dict['*'] = 2
priority_dict['/'] = 2
priority_dict['+'] = 1
priority_dict['-'] = 1

input_string = input().rstrip()
stack = deque()

for ch in input_string:
    if (ch.isalpha()):
        print(ch, end='')
    else:
        process_operator(ch)

while(stack):
    print(stack.pop(), end='')