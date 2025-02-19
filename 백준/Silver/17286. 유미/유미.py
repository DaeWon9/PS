import sys
input = sys.stdin.readline

def calc_distance(pos1, pos2):
    return ((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2) ** 0.5

datas = []

for _ in range(4):
    datas.append(tuple(map(int, input().split())))

answer = 2147483647

for combi in ['0123','0132','0213','0231','0312','0321']:
    temp_sum = 0
    for i in range(3):
        s, e = int(combi[i]), int(combi[i+1])
        temp_sum += calc_distance(datas[s], datas[e])
    
    if (answer > temp_sum):
        answer = temp_sum

print(int(answer))