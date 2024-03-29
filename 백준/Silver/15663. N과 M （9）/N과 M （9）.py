import sys
input = sys.stdin.readline

def solution(combi):
    if (len(combi) == M):
        print(*combi)
        return
    
    prev_num = 0
    for i in range(1, N + 1):
        if (prev_num == num_list[i]):
            continue
        if (i in visited):
            continue
        
        prev_num = num_list[i]
        combi.append(num_list[i])
        visited.add(i)
        solution(combi)
        combi.pop()
        visited.remove(i)

N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
num_list.sort()
visited = set()

solution([])