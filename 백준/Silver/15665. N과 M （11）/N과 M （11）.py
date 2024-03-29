import sys
input = sys.stdin.readline

def solution(combi, pivot):
    if (len(combi) == M):
        print(*combi)
        return
    
    prev_num = 0
    for i in range(1, N + 1):
        if (prev_num == num_list[i]):
            continue
        
        prev_num = num_list[i]
        combi.append(num_list[i])
        solution(combi, i)
        combi.pop()

N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
num_list.sort()

solution([], 1)