import sys
input = sys.stdin.readline

def isGoodWord(string):
    stack = []

    for char in string:
        if (not stack):
            stack.append(char)
            continue

        if (stack[-1] == char):
            stack.pop()
        else:
            stack.append(char)
        
    if (stack):
        return False
    
    return True

N = int(input())
answer = 0

for i in range(N):
    if (isGoodWord(input().rstrip())):
        answer += 1

print(answer)