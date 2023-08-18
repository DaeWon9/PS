import sys

people_count, party_count = map(int, sys.stdin.readline().split())

truth_know_people = set(list(map(int, sys.stdin.readline().split()))[1:])

party_attended_people_list = list()

visited = [False] * party_count

for _ in range(party_count):
    input_list = list(map(int, sys.stdin.readline().split()))[1:]
    party_attended_people_list.append(set(input_list))

while True:
    count = 0
    for index in range(party_count):
        if not visited[index] and set(party_attended_people_list[index]).intersection(
            truth_know_people
        ):
            visited[index] = True
            count += 1
            for item in set(party_attended_people_list[index]).difference(
                truth_know_people
            ):
                truth_know_people.add(item)

    if count == 0:
        break

print(visited.count(False))