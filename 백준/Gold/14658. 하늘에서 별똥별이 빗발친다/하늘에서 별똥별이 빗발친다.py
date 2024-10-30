import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
answer= 0
stars = []
for _ in range(K):
    x, y = map(int, input().split())
    stars.append([x, y])

stars.sort()

for x, y in stars: # x 기준
    x1 = x
    x2 = x + L

    target_stars_y = sorted([y for x, y in stars if (x1 <= x <= x2)])

    left = 0

    for right in range(len(target_stars_y)):
        
        while True:
            if (target_stars_y[right] - target_stars_y[left] <= L):
                break
            left += 1

        if (answer < right - left + 1):
            answer = right - left + 1

print(K - answer)
