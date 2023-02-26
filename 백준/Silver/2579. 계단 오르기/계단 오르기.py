N = int(input())

stair_dict = dict()
max_stair_dict = dict()

for i in range(N):
    stair_dict[i] = int(input())

if N == 1:
    print(stair_dict[0])
elif N == 2:
    print(stair_dict[0]+stair_dict[1])
elif N == 3:
    print(max(stair_dict[0]+stair_dict[2], stair_dict[1]+stair_dict[2]))
else:
    max_stair_dict[0] = stair_dict[0]
    max_stair_dict[1] = stair_dict[0]+stair_dict[1]
    max_stair_dict[2] = max(stair_dict[0]+stair_dict[2], stair_dict[1]+stair_dict[2])

    for i in range(3, N):
        max_stair_dict[i] = max(max_stair_dict[i - 3] + stair_dict[i] + stair_dict[i - 1], max_stair_dict[i - 2] + stair_dict[i])

    print(max_stair_dict[N-1])