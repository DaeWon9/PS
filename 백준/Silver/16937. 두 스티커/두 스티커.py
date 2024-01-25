import sys
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())

stickers = []
for _ in range(n):
    stickers.append(list(map(int, input().split())))

result = 0
for i in range(n):
    for j in range(i + 1, n):
        r1, c1 = stickers[i]
        r2, c2 = stickers[j]

        # case 1
        if (r1 + r2 <= h and max(c1, c2) <= w) or (max(r1, r2) <= h and c1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        
        # case 2
        if (c1 + r2 <= h and max(r1, c2) <= w) or (max(c1, r2) <= h and r1 + c2 <= w):
            result = max(result, r1*c1 + r2*c2)
        
        # case 3
        if (c1 + c2 <= h and max(r1, r2) <= w) or (max(c1, c2) <= h and r1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)
        
        # case 4
        if (r1 + c2 <= h and max(c1, r2) <= w) or (max(r1, c2) <= h and c1 + r2 <= w):
            result = max(result, r1*c1 + r2*c2)

print(result) 