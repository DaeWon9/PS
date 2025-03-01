from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    
    group_size = {}
    group_id_map = [[-1] * m for _ in range(n)]  
    group_id = 0

    direction_x = [0, 0, 1, -1]
    direction_y = [1, -1, 0, 0]

    # BFS로 그룹화
    def bfs(sr, sc):
        q = deque([(sr, sc)])
        group_id_map[sr][sc] = group_id
        size = 1

        while q:
            r, c = q.popleft()
            for i in range(4):
                dr, dc = r + direction_y[i], c + direction_x[i]
                if 0 <= dr < n and 0 <= dc < m and land[dr][dc] == 1 and group_id_map[dr][dc] == -1:
                    group_id_map[dr][dc] = group_id
                    q.append((dr, dc))
                    size += 1
        
        return size

    for r in range(n):
        for c in range(m):
            if land[r][c] == 1 and group_id_map[r][c] == -1:
                group_size[group_id] = bfs(r, c)
                group_id += 1

    # 각 열에서 최대 그룹 크기 찾기
    answer = 0
    for c in range(m):
        unique_groups = set()
        for r in range(n):
            if group_id_map[r][c] != -1:
                unique_groups.add(group_id_map[r][c])
        
        total_size = sum(group_size[g] for g in unique_groups)
        answer = max(answer, total_size)

    return answer
