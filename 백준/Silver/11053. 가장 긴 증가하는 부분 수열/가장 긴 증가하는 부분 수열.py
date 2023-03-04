import sys

N = int(sys.stdin.readline())
input_array = list(map(int, sys.stdin.readline().rstrip().split(" ")))

length_list = [1 for _ in range(N)]

for i in range(N): 
    for j in range(i):
        if input_array[i] > input_array[j]:
            length_list[i] = max(length_list[i], length_list[j] + 1)

print(max(length_list))