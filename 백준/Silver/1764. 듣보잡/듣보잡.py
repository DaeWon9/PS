import sys

N,M = map(int, input().split(" "))

not_listen_people = dict()
not_listen_see_people = []
count = 0

for _ in range (N):
    name = sys.stdin.readline().rstrip()
    not_listen_people[name] = True

for _ in range(M):
    name = sys.stdin.readline().rstrip()

    try:
        if (not_listen_people[name]):
            not_listen_see_people.append(name)
            count = count + 1
    except:
        pass

not_listen_see_people = sorted(not_listen_see_people)
print(count)
for name in not_listen_see_people:
    print(name)