import sys
input = sys.stdin.readline

N = int(input())
hp_list = [0] + list(map(int, input().split()))
value_list = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(101)] for _ in range(N + 1)]

for person_id in range(1, N + 1):
    for hp in range(101):
        added_value = value_list[person_id]
        lose_hp = hp_list[person_id]

        if (hp >= lose_hp):
            dp[person_id][hp] = max(dp[person_id - 1][hp - lose_hp] + added_value, dp[person_id - 1][hp])
        else:
            dp[person_id][hp] = dp[person_id - 1][hp]

print(dp[N][99])