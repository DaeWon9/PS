import sys
input = sys.stdin.readline

L, R = map(str, input().split())
answer = 0

if (len(L) != len(R)): # 자리수가 바뀌면, 10, 100, 1000 등 8이 아예 없는 경우가 존재
    print(0)
    exit(0)

for i in range(len(L)): # 길이가 같으면 각자리 비교하고, 둘다 8이여야 무조건 8
    if (L[i] == '8' and R[i] == '8'):
        answer += 1
    elif (L[i] != R[i]):
        break

print(answer)

