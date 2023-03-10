import sys

def check_bingo(bingo):
    count = 0

    if (bingo[1] and bingo[7] and bingo[13] and bingo[19] and bingo[25]):
        count += 1
    if (bingo[5] and bingo[9] and bingo[13] and bingo[17] and bingo[21]):
        count += 1
    for i in range(5):
        if (bingo[i*5 + 1] and bingo[i*5 + 2] and bingo[i*5 + 3] and bingo[i*5 + 4] and bingo[i*5 + 5]):
            count += 1
    for i in range(1,6):
        if (bingo[i] and bingo[i + 5] and bingo[i + 10] and bingo[i + 15] and bingo[i + 20]):
            count += 1
    
    return count

bingo = dict()
copy_bingo = dict()

for i in range(5):
    count = 1
    for number in list(map(int, sys.stdin.readline().rstrip().split(" "))):
        bingo[i*5 + count] = False
        copy_bingo[number] = i*5 + count
        count += 1

call_number = []
for i in range(5):
    for number in list(map(int, sys.stdin.readline().rstrip().split(" "))):
        call_number.append(number)

call_count = 0
for number in call_number:
    call_count += 1
    bingo[copy_bingo[number]] = True
    bingo_count = check_bingo(bingo)
    if (bingo_count > 2):
        break

print(call_count)