N = int(input())

if (N < 3):
    print(-1)
else:
    count = 0
    while(N > 2):
        if (N % 5 == 0):
            count = count + N//5
            break
        else:
            N = N - 3
            count = count + 1
    if (N == 1 or N == 2):
        print(-1)
    else:
        print(count)