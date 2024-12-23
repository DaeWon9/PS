import sys
input = sys.stdin.readline

while True:
    M, A, B = map(int, input().split())

    if (M == 0 and A == 0 and B == 0):
        break
    
    diff = round((M / A - M / B) * 3600)
    hour = diff // 3600
    minute = (diff % 3600) // 60
    second = diff % 60

    print("%d:%02d:%02d" % (hour, minute, second))