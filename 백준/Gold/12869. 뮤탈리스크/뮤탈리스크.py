import sys
input = sys.stdin.readline

N = int(input())
hps = list(map(int, input().split())) + [0] * (3-N)
attack_cases = [(-9, -3, -1), (-9, -1, -3), (-3, -9, -1), (-3, -1, -9), (-1, -9, -3), (-1, -3, -9)]
# dp[hp1][hp2][hp3] = 최소 공격 횟수
dp = [[[61 for _ in range(61)] for _ in range(61)] for _ in range(61)]
dp[hps[0]][hps[1]][hps[2]] = 0

# 60 * 60 * 60 * 6 = 1,296,000
for hp1 in range(60, -1, -1):
    for hp2 in range(60, -1, -1):
        for hp3 in range(60, -1, -1):
            for dhp1, dhp2, dhp3 in attack_cases:
                new_hp1 = hp1 + dhp1
                new_hp2 = hp2 + dhp2
                new_hp3 = hp3 + dhp3

                if (new_hp1 < 0):
                    new_hp1 = 0

                if (new_hp2 < 0):
                    new_hp2 = 0

                if (new_hp3 < 0):
                    new_hp3 = 0

                if (dp[new_hp1][new_hp2][new_hp3] > dp[hp1][hp2][hp3] + 1):
                    dp[new_hp1][new_hp2][new_hp3] = dp[hp1][hp2][hp3] + 1

print(dp[0][0][0])