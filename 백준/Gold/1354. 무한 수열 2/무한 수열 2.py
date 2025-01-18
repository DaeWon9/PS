import sys
input = sys.stdin.readline

def solve(N):
    if (N in A):
        return A[N]
    A[N] = solve(max(0, N // P - X)) + solve(max(0, N // Q - Y))
    return A[N]

N, P, Q, X, Y = map(int, input().split())
A = {}
A[0] = 1
A[1] = 2

print(solve(N))