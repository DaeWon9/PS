import sys
input = sys.stdin.readline

def solution(combi, pivot):
    if len(combi) == M:
        print(*combi)
        return
    
    prev_num = 0
    for i in range(pivot, N + 1):
        if prev_num == num_list[i]:
            continue
        
        prev_num = num_list[i]
        combi.append(num_list[i])
        solution(combi, i + 1)
        combi.pop()

N, M = map(int, input().split())
num_list = [0] + sorted(map(int, input().split())) 
visited = set()

solution([], 1)