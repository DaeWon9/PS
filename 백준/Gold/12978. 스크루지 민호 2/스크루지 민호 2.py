import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def solve(v, p):
    if (dp[v][0] != -1 and dp[v][1] != -1):
        return dp[v][0], dp[v][1]
    
    dp[v][0] = 0
    dp[v][1] = 1

    for adj_vertex in adj_vertices[v]:
        if (adj_vertex == p):
            continue

        not_build, build = solve(adj_vertex, v) 

        dp[v][0] += build
        dp[v][1] += min(not_build, build)

    return dp[v][0], dp[v][1]

# tree
N = int(input()) # (2 ≤ N ≤ 100,000) 
adj_vertices = defaultdict(list)

for _ in range(N-1):
    u, v = map(int, input().split())

    adj_vertices[u].append(v)
    adj_vertices[v].append(u)

dp = [[-1 for _ in range(2)] for _ in range(N+1)]
print(min(solve(1, 0)))