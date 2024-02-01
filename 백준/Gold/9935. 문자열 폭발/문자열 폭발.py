import sys
from collections import deque
input = sys.stdin.readline

def bomb():
    for _ in range(len(bomb_string)):
        bomb_stack.pop()

def is_top_bomb_string():
    if (len(bomb_stack) < len(bomb_string)):
        return False
    for i in range(len(bomb_string)):
        if (bomb_stack[-(i + 1)] != bomb_string[-(i + 1)]):
            return False
    return True

input_string = input().rstrip()
bomb_string = input().rstrip()
last_bomb_char = bomb_string[-1]

string_stack = deque()
bomb_stack = deque()

for ch in input_string:
    if (ch in bomb_string):
        bomb_stack.append(ch)
        if (ch == last_bomb_char and is_top_bomb_string()):
            bomb()
    else:
        while bomb_stack:
            string_stack.append(bomb_stack.popleft())
        string_stack.append(ch)

if not string_stack and not bomb_stack:
    print("FRULA")
else:
    while string_stack:
        print(string_stack.popleft(), end='')
    while bomb_stack:
        print(bomb_stack.popleft(), end='')