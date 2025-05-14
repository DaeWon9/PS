import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input()) # 동전의 종류 N(1 ≤ N ≤ 100)
    coins = []
    total = 0

    for _ in range(N):
        coin, count = map(int, input().split())
        total += coin * count
        coins.append((coin, count))

    if (total % 2 == 1): # 총 합이 홀수이면 쪼개기 불가능
        print(0)
        continue

    target = total // 2
    # dp[i 금액을 만드는게 가능한가?]
    # 최종 목적인 dp[target]이 만들어진다는 것은, 그 나머지도 같이 만들어진다는 소리
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1

    # dp[target] == 1 ?
    for coin, count in coins:        
        for c in range(target, coin-1, -1):
            if (dp[c-coin] == 0):
                continue

            for i in range(1, count+1):
                if (c - coin + coin * i < target + 1):
                    dp[c - coin + coin * i ] = 1
                else:
                    break
                        
    print(dp[target])
