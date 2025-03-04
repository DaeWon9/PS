from collections import deque, defaultdict
    
def solution(storage, requests):
    def is_movable(n, m, r, c):
        return (0 <= r < n and 0 <= c < m)

    def is_border(n, m, sr, sc):
        queue = deque([(sr, sc)])
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[sr][sc] = True
        
        while queue:
            r, c = queue.popleft()
            
            for i in range(4):
                dr = r + direction_y[i]
                dc = c + direction_x[i]
                
                if (not is_movable(n, m, dr, dc)):
                    return True
                
                if (visited[dr][dc]):
                    continue
                    
                visited[dr][dc] = True
                
                if ((dr, dc) in removed_pos_set):
                    queue.append((dr, dc))
                    
        return False
    
    direction_x = [0, 0, 1, -1]
    direction_y = [1, -1, 0, 0]
    n, m = len(storage), len(storage[0])
    alpha_dict = defaultdict(set)
    answer = n*m
    removed_pos_set = set()
    
    for r in range(n):
        for c in range(m):
            alpha_dict[storage[r][c]].add((r, c))
    
    for request in requests:
        request_len = len(request)
        target = request[0]
        result_list = []
        
        if (request_len == 1):
            for r, c in alpha_dict[target]:           
                if (is_border(n, m, r, c)):
                    result_list.append((r, c))
        else:
            result_list = list(alpha_dict[target])
            
        answer -= len(result_list)
        for r, c in result_list:
            removed_pos_set.add((r, c))
            alpha_dict[target].remove((r, c))

    return answer