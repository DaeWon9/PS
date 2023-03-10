N = int(input())
F = int(input())

snail_list = []
row = N // 2
col = N // 2
snail_list = [[0 for i in range(N)] for i in range(N)]
snail_list[row][col] = 1
count = 2

for i in range(1, N//2 + 1):
    for j in range(i*2):
        snail_list[row-i][col+j-i+1] = count
        count += 1
    for j in range(i*2):
        snail_list[row+j-i+1][col+i] = count
        count += 1
    for j in range(i*2):
        snail_list[row+i][col-j+i-1] = count
        count += 1
    for j in range(i*2):
        snail_list[row-j+i-1][col-i] = count
        count += 1

for item in snail_list:
    for num in item:
        print(num, end=" ")
    print("")

target_index = [(i + 1, j + 1) for i in range(N) for j in range(N) if snail_list[i][j] == F]
print(target_index[0][0], target_index[0][1])