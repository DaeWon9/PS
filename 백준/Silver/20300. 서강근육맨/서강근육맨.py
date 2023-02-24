import sys

N = int(input())
loss_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
loss_list.sort()

loss_sum_list = []
if (N % 2 == 0):
    for i in range(0, N // 2):
        loss_sum_list.append(loss_list[i] + loss_list[-(i+1)])
    print(max(loss_sum_list))
else:
    loss_sum_list.append(loss_list[-1])
    for i in range(0, N // 2):
        loss_sum_list.append(loss_list[i] + loss_list[-(i+2)])
    print(max(loss_sum_list))