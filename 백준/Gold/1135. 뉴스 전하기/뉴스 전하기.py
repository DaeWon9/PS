import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solve(root):
    children_count = len(children[root])
    result_list = []

    if (children_count == 0): # leaf
        return 0

    for child in children[root]:
        tmp_value = solve(child)
        result_list.append(tmp_value)

    result_list.sort(reverse=True) # 가장 오래 걸리는 자식부터 방문

    answer = 0
    for i in range(children_count):
        tmp_answer = result_list[i] + i + 1
        if (answer < tmp_answer):
            answer = tmp_answer
            
    return answer

N = int(input())
A = list(map(int, input().split()))
children = defaultdict(list)

for i in range(1, N): # i의 부모는 A[i] -> A[i]의 자식은 i
    children[A[i]].append(i)

print(solve(0))