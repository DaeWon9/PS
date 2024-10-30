import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())
stars = []
for _ in range(K):
    x, y = map(int, input().split())
    stars.append([x, y])

answer = 0
for i in range(K):
    for j in range(K):
        count = 0
        for x, y in stars:
            if (stars[i][1] <= y <= stars[i][1] + L and stars[j][0] <= x <= stars[j][0] + L):
                count += 1
        
        if (answer < count):
            answer = count

print(K - answer)