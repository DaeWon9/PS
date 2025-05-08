import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# Tree 구조에서
# case_1 부모가 우수마을이면 -> 자식은 우수마을이 아님
# case_2 부모가 우수마을이 아니면 -> 자식은 우수마을 or 우수마을 x
# case_1, case_2를 구해서 그 중 최대가 answer

def solve(cur, parent):
    if (dp[cur][0] != -1 and dp[cur][1] != -1):
        return dp[cur][0], dp[cur][1]
    
    dp[cur][0] = 0
    dp[cur][1] = sizes[cur]
    
    for next in adj_vertices[cur]: 
        if (next == parent):
            continue
            
        child_not_best, child_best = solve(next, cur)
        # 현재 노드가 우수 마을이 아닌 경우 -> 자식은 우수 마을일 수도, 아닐 수도 있음
        dp[cur][0] += max(child_not_best, child_best)
        # 현재 노드가 우수 마을인 경우 -> 자식은 우수 마을이 아니어야 함
        dp[cur][1] += child_not_best
    
    return dp[cur][0], dp[cur][1]

N = int(input()) # (1 ≤ N ≤ 10,000)
sizes = [0] + list(map(int, input().split()))
adj_vertices = defaultdict(list)

for _ in range(N-1):
    u, v = map(int, input().split())
    adj_vertices[u].append(v)
    adj_vertices[v].append(u)

# dp[i][0]: i번 마을이 우수 마을이 아닌 경우의 최대 주민 수
# dp[i][1]: i번 마을이 우수 마을인 경우의 최대 주민 수
dp = [[-1 for _ in range(2)] for _ in range(N+1)]

not_best, best = solve(1, 0)
print(max(not_best, best))
