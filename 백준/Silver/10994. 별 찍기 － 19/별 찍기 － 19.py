N = int(input())

star_table = [[' '] * (1 + (N-1)*4) for _ in range(1 + (N-1)*4)]

def assign_star(N, index):
    if N == 1:
        star_table[index][index] = "*"
        return
    
    for i in range(index, index + 1 + (N-1)*4):
        star_table[index][i] = "*"
        star_table[index + ((N-1)*4)][i] = "*"

        star_table[i][index] = "*"
        star_table[i][index + ((N-1)*4)] = "*"

    return assign_star(N-1, index+2)

assign_star(N, 0)

for i in range(1 + (N-1)*4):
    for j in range(1 + (N-1)*4):
        print(star_table[i][j], end="")
    print("")