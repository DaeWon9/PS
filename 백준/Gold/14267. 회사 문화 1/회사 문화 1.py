import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] + list(map(int, input().split()))
answer = [0] * (n+1)

for _ in range(m):
    i, w = map(int, input().split())
    answer[i] += w

# 직속 상사의 번호는 자신의 번호보다 작으며, 최종적으로 1번이 사장이다.
for i in range(2, n+1):
    answer[i] += answer[parent[i]]

print(*answer[1:])