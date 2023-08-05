import sys

n = int(sys.stdin.readline())
total_people_count = 0
villages = []

for _ in range(n):
    pos, people_count = sys.stdin.readline().split()
    total_people_count += int(people_count)
    villages.append((int(pos), int(people_count)))

villages.sort(key=lambda x: x[0])

half_people_count = total_people_count // 2

people_count = 0
for village in villages:
    people_count += village[1]
    if people_count > half_people_count:
        print(village[0])
        break
