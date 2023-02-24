T = int(input())

fibo_dict = dict()
fibo_dict[0] = [1,0]
fibo_dict[1] = [0,1]
fibo_dict[2] = [1,1]

for _ in range(T):
    zero_count = 0
    one_count = 0
    min_key = 1

    N = int(input())
    
    if (N > 2):
        while(min_key <= N - 2):
            fibo_dict[min_key + 1] = [(fibo_dict[min_key][0] + fibo_dict[min_key - 1][0]),(fibo_dict[min_key][1] + fibo_dict[min_key - 1][1])]
            min_key += 1
        zero_count = (fibo_dict[N-2][0] * 2) + fibo_dict[N-3][0]
        one_count = (fibo_dict[N-2][1] * 2) + fibo_dict[N-3][1]
        print(zero_count, one_count)
    else:
        print(fibo_dict[N][0], fibo_dict[N][1])
