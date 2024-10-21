import sys
from collections import defaultdict
input = sys.stdin.readline

def update(i, diff):
    while i <= N:
        tree[i] += diff
        i += (i & -i)

def prefix_sum(i): # 1 ~ i
    sum = 0

    while i > 0:
        sum += tree[i]
        i -= (i & -i)

    return sum

def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start - 1)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

num_dict = defaultdict(int)
for i in range(N):
    num_dict[B[i]] = i + 1

arr = []
for i in range(N):
    arr.append(num_dict[A[i]])

tree = [0 for _ in range(N + 1)]

answer = 0
for num in arr:
    update(num, 1)
    answer += interval_sum(num + 1, N)

print(answer)