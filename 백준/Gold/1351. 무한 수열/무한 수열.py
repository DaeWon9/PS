import sys
from collections import defaultdict
input = sys.stdin.readline

def solve(N):
    if (N in A):
        return A[N]
    A[N] = solve(N // P) + solve(N // Q)
    return A[N]

N, P, Q = map(int, input().split())
A = defaultdict(int)
A[0] = 1
A[1] = 2

print(solve(N))