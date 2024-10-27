import sys
from collections import deque
input = sys.stdin.readline

def solution(N, scores):
    # dp[i][j]: i점일 때 j번 팔굽혀펴기 가능 여부
    dp = [[False for _ in range(5555)] for _ in range(555)]

    queue = deque()
    answer = -1

    for score in scores:
        queue.append((score, score, score))
        dp[score][score] = True

    while queue:
        score_sum, added_count, whole_count = queue.popleft()

        if (whole_count == N and answer < score_sum):
            answer = score_sum

        for score in scores:
            new_score_sum = score_sum + score
            new_added_count = added_count + score
            new_whole_count = whole_count + new_added_count

            if (new_whole_count > N or dp[new_score_sum][new_whole_count]):
                continue

            queue.append((new_score_sum, new_added_count, new_whole_count))
            dp[new_score_sum][new_whole_count] = True

    return answer

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    scores = list(map(int, input().split()))

    print(solution(N, scores))