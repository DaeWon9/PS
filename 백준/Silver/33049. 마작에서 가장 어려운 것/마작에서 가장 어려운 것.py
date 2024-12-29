import sys
input = sys.stdin.readline

P3, P4, P0 = map(int, input().split())
for PP4 in range(P0, -1, -1):
    PPP4 = P4 + PP4
    PPP3 = P3 + P0 - PP4
    if (PPP4 % 4 == 0 and PPP3 % 3 == 0):
        print(PPP3 // 3, PPP4 // 4)
        exit(0)

print(-1)
