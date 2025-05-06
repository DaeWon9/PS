import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())  # 최대 레벨 (1 ≤ N ≤ 50)
character_counts = list(map(int, input().split()))  # 각 레벨에 있는 캐릭터 수
character_powers = list(map(int, input().split()))  # 각 레벨의 전투력
D = int(input())  # 훈련 가능 일수 (1 ≤ D ≤ 100)

# dp[i][j][k] =
# i: 남은 훈련 일수
# j: 현재 레벨
# k: 전 레벨에서 훈련되어 넘어온 인원 수
# dp[i][j][k]: i일이 남았고, 현재 레벨이 j이며, k명이 도달해 있을 때 얻을 수 있는 최대 추가 전투력
dp = [[[-1 for _ in range(101)] for _ in range(N)] for _ in range(101)]

def getDp(day, level, arrived):
    if (level == N - 1):
        return 0
    
    if (dp[day][level][arrived] != -1):
        return dp[day][level][arrived]

    max_power = 0
    for i in range(arrived + character_counts[level] + 1):
        if (day < i):
            break

        gain = (character_powers[level + 1] - character_powers[level]) * i
        next_power = getDp(day - i, level + 1, i)
        max_power = max(max_power, gain + next_power)

    dp[day][level][arrived] = max_power
    return max_power

initial_power = sum(character_counts[i] * character_powers[i] for i in range(N))
print(initial_power + getDp(D, 0, 0))
