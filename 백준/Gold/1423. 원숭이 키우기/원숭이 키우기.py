import sys
input = sys.stdin.readline

N = int(input())  # 최대 레벨 (1 ≤ N ≤ 50)
character_counts = list(map(int, input().split()))  # 각 레벨에 있는 캐릭터 수
character_powers = list(map(int, input().split()))  # 각 레벨의 전투력
D = int(input())  # 훈련 가능 일수 (1 ≤ D ≤ 100)

init_power = sum(character_counts[i] * character_powers[i] for i in range(N))

# 각 레벨에서 훈련 가능한 캐릭터 수는 D일을 넘을 수 없음
for i in range(N):
    character_counts[i] = min(character_counts[i], D)

# dp[d]: d일을 사용했을 때 최대 추가 전투력
dp = [0] * (D + 1)

for level in range(N):
    for _ in range(character_counts[level]):
        # dp[j]를 뒤에서부터 순회해야 중복 훈련 방지
        for used_days in range(D, -1, -1):
            for next_level in range(level + 1, N):
                required_days = used_days + (next_level - level)
                if (required_days > D):
                    break
                gain = character_powers[next_level] - character_powers[level]
                dp[required_days] = max(dp[required_days], dp[used_days] + gain)

print(init_power + dp[-1])
