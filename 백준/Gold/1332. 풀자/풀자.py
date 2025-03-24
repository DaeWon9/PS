import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(idx, mn, mx, cnt):
    global ans
    if ((idx, mn, mx) in visited): 
        return
    visited.add((idx, mn, mx))

    if (cnt >= ans):
        return
    if (mx - mn >= V):
        ans = min(ans, cnt)
        return

    # A+2 이동
    if (idx + 2 < N):
        solve(idx + 2, min(mn, arr[idx + 2]), max(mx, arr[idx + 2]), cnt + 1)

    # A+1 이동
    if (idx + 1 < N):
        solve(idx + 1, min(mn, arr[idx + 1]), max(mx, arr[idx + 1]), cnt + 1)

N, V = map(int, input().split())
arr = list(map(int, input().split()))

visited = set()
ans = N

solve(0, arr[0], arr[0], 1)
print(ans)
