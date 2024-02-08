import sys
from bisect import insort_left
input = sys.stdin.readline

def solution(num_list):
    sorted_list = []
    answer = []

    for index, num in enumerate(num_list):
        insort_left(sorted_list, num)

        if ((index + 1) % 2 == 1):
            answer.append(sorted_list[index // 2])

    return answer

T = int(input())

for _ in range(T):
    M = int(input())

    num_list = list(map(int, input().split()))
    for i in range(M // 10):
        plus_list = list(map(int, input().split()))
        for num in plus_list:
            num_list.append(num)

    result = solution(num_list)
    print(len(result))
    for index, num in enumerate(result):
        if (index % 10 == 9):
            print(num)
        else:
            print(num, end=' ')
