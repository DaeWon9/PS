import sys

N, M, B = map(int, sys.stdin.readline().split())
area_list = []

for i in range(N):
    area_list.append(list(map(int, sys.stdin.readline().split())))

min_height = min(map(min, area_list))
max_height = max(map(max, area_list))

if (min_height < 0):
    min_height = 0
if (max_height > 256):
    max_height = 256

result = []

for height in range(min_height, max_height + 1):

    available_block = B
    time = 0

    for area in area_list:
        for region in area:
            height_difference = region - height
            if height_difference > 0 : # type1 -> time : 2
                available_block += height_difference
                time += 2 * height_difference
            else: # type2 -> time : 1
                available_block -= abs(height_difference)
                time += abs(height_difference)
    
    if available_block > -1:
        result.append((time, height))

result.sort(key=lambda x:(x[0],-x[1]))
print(result[0][0], result[0][1])