computer_count = int(input())
N = int(input())
virus_dict = dict()
connect_set = set()

for _ in range(N):
    key, value = map(int, input().split(" "))
    if (key not in virus_dict.keys()):
        virus_dict[key] = [value]
    else:
        new_value = []
        for item in virus_dict[key]:
            new_value.append(item)
        new_value.append(value)
        virus_dict[key] = list(set(new_value))

    if (value not in virus_dict.keys()):
        virus_dict[value] = [key]
    else:
        new_value = []
        for item in virus_dict[value]:
            new_value.append(item)
        new_value.append(key)
        virus_dict[value] = list(set(new_value))

connect_set = set(virus_dict[1])

for _ in range (computer_count):
    for connect_key in connect_set:
        try:
            connect_set = connect_set.union(virus_dict[connect_key])
        except:
            pass

connect_set = connect_set - {1}
print(connect_set)
print(len(connect_set))
