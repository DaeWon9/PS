import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

count_dict = defaultdict(int)
stack = []
answer = [-1] * N

for num in A:
    count_dict[num] += 1

for i in range(N):
    while (stack and count_dict[A[stack[-1]]] < count_dict[A[i]]):
        top = stack.pop()
        answer[top] = A[i]
        
    stack.append(i)

print(*answer)
