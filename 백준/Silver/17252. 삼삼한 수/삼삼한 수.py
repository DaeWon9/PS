import sys
input = sys.stdin.readline

N = int(input())
answer = "YES"

if (N == 0):
    print("NO")
    exit(0)

while(True):
    if (N < 3):
        break

    remainder = N % 3
    N = N // 3

    if (remainder == 2 or N == 2):
        answer = "NO"
        break

print(answer)