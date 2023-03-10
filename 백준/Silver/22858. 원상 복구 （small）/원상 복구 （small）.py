import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
S = list(map(int, sys.stdin.readline().rstrip().split()))
D = list(map(int, sys.stdin.readline().rstrip().split()))

for _ in range(K):
    temp = S.copy()
    for i in range(N):
        S[D[i]-1] = temp[i]

for item in S:
    print(item, end=" ")