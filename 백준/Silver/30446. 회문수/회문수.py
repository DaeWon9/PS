import sys
input = sys.stdin.readline

def solve(N):
    arr = [0, 9, 9, 90, 90, 900, 900, 9000, 9000, 90000, 90000]
    res = 0
    len_n = len(N)

    if len_n == 1:
        print(int(N))
    else:
        for i in range(len_n):
            res += arr[i]

        if (len_n % 2) != 0:  # 홀
            tmp = 10 ** (len_n // 2)
            while True:
                s = str(tmp)
                e = str(tmp)[:-1][::-1]
                pal = s + e

                if int(pal) <= int(N):
                    tmp += 1
                    res += 1
                else:
                    break
            print(res)
            sys.exit()
        else: # 짝
            tmp = 10 ** (len_n // 2-1)
            while True:
                s = str(tmp)
                e = str(tmp)[::-1]
                pal = s + e

                if int(pal) <= int(N):
                    tmp += 1
                    res += 1
                else:
                    break
            print(res)
            sys.exit()

N = int(input().rstrip())
solve(str(N))