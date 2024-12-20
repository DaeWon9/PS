import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())

A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = [A[i] + B[j] for i in range(n) for j in range(n)]
CD = [C[i] + D[j] for i in range(n) for j in range(n)]

CD_counter = Counter(CD)
answer = sum(CD_counter[-ab] for ab in AB)

print(answer)
