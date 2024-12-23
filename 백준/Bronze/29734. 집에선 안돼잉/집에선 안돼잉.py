import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T, S = map(int, input().split())
zip_time = N + (N // 8 - (1 if N % 8 == 0 else 0)) * S
dok_time = T + M + (M // 8 - (1 if M % 8 == 0 else 0)) * (S + 2 * T)

if (dok_time < zip_time):
    print('Dok')
    print(dok_time)
else:
    print('Zip')
    print(zip_time)