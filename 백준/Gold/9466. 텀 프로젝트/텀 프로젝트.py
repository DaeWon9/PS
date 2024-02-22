import sys
from collections import deque, defaultdict
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    answer = n
    visited = [False for _ in range(n + 1)]
    input_data = list(map(int, input().split()))
    
    for id in range(1, n + 1):
        if (visited[id]):
            continue

        index_dict = defaultdict(lambda : -1)

        team_count = 1
        index_dict[id] = 0
        
        queue = deque()
        queue.append(id)
        visited[id] = True

        while queue:
            v = queue.popleft()
            choice = input_data[v - 1]
            
            if (index_dict[choice] != -1):
                start_index = index_dict[choice]
                if (team_count - start_index > 0):
                    answer -= (team_count - start_index)
                break

            if (not visited[choice]):
                queue.append(choice)
                index_dict[choice] = team_count
                team_count += 1
                visited[choice] = True
                    
    print(answer)