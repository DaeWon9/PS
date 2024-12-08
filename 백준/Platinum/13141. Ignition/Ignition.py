import sys
input = sys.stdin.readline

# 점화되는 시간을 구하기 위해 플로이드-워셜
# 점화된 후 가장 긴 간선을 태우는 시간 계산.
# a-b 간선이 있을 때, a, b 정점에 모두 점화 후 -> 남은 거리 2배로 감소

N, M = map(int, input().split())
distance = [[2147483647 for _ in range(N)] for _ in range(N)]
max_distance = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    distance[i][i] = 0

for _ in range(M):
    s, e, l = map(int, input().split()) # 1 ≤ L ≤ 100
    s -= 1
    e -= 1
    if (distance[s][e] > l):
        distance[s][e] = distance[e][s] = l
    if (max_distance[s][e] < l):
        max_distance[s][e] = max_distance[e][s] = l

for k in range(N):
    for i in range(N):
        for j in range(N):
            if (distance[i][j] > distance[i][k] + distance[k][j]):
                distance[i][j] = distance[i][k] + distance[k][j]

answer = 2147483647 # find min
for pivot in range(N):
    tmp_answer = 0

    # 각 그룹 체크 후 max치가 전체 그래프가 타는 시간
    for i in range(N):
        for j in range(N):
            if (max_distance[i][j] == 0):
                continue
            
            pivot_to_i = distance[pivot][i]
            pivot_to_j = distance[pivot][j]

            # 양 끝 정점이 모두 점화 되었을 때, 남은 길이
            remain_dist = max_distance[i][j] - abs(pivot_to_i - pivot_to_j)

            # 점화가 늦은 정점 시간 + 남은거리의 절반 (두배로 빨리 없어짐)
            updated_tmp_answer = max(pivot_to_i, pivot_to_j) + (remain_dist / 2)
            if (tmp_answer < updated_tmp_answer):
                tmp_answer = updated_tmp_answer

    if (answer > tmp_answer): 
        answer = tmp_answer

print(answer)