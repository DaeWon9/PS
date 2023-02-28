N = int(input())

fibo = dict()

fibo[0] = 0
fibo[1] = 1

if N > 1:
    for i in range(2,N+1):
        fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[N])