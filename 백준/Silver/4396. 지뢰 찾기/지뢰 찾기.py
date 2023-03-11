import sys

def count_surrounding_mine(mine_list, row, col):
    count = 0
    if (mine_list[row][col] == "*"):
        return "*"
    
    if (col > 0 and mine_list[row][col - 1] == "*"):
        count += 1
    if (col < n-1 and mine_list[row][col + 1] == "*"):
        count += 1

    if (col > 0 and row > 0 and mine_list[row - 1][col - 1] == "*"):
        count += 1
    if (row > 0 and mine_list[row - 1][col] == "*"):
        count += 1
    if (row > 0 and col < n-1 and mine_list[row - 1][col + 1] == "*"):
        count += 1

    if (col > 0 and row < n-1 and mine_list[row + 1][col - 1] == "*"):
        count += 1
    if (row < n-1 and mine_list[row + 1][col] == "*"):
        count += 1
    if (row < n-1 and col < n-1 and mine_list[row + 1][col + 1] == "*"):
        count += 1
    return count

n = int(sys.stdin.readline())
mine_list = []

for _ in range(n):
    mine_list.append(sys.stdin.readline().rstrip())

input_list = []
for _ in range(n):
    input_list.append(sys.stdin.readline().rstrip())

result_list = []
is_mined = False
for i in range(n):
    result_string = ""
    for j in range(n):
        if (input_list[i][j] == "x"):
            count = count_surrounding_mine(mine_list, i, j)
            if (count == "*"):
                is_mined = True
            result_string = result_string + str(count)
        else:
            if (mine_list[i][j] == "*"):
                result_string = result_string + "*"
            else:
                result_string = result_string + "."
    result_list.append(result_string)    

for result in result_list:
    if (is_mined):
        print(result)
    else:
        print(str(result).replace("*", "."))
