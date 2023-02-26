N, K = map(int, input().split(" "))

coin = []
for i in range (N):
    coin.append(int(input()))

coin = sorted(coin, reverse=True)

count = 0
for i in coin:
    if (K // i >= 1):
        count = count + K // i

    if (K % i == 0):
        break

    K = K % i

print(count)