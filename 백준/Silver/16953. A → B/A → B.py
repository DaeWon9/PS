A, B = map(int, input().split(" "))

parent = [A]
count = 1

while(B not in parent):
    leaf = []
    for item in parent:
        if (int(str(item) + "1") <= B):
            leaf.append(int(str(item) + "1"))
        if (item * 2 <= B):
            leaf.append(item * 2)

    parent = list(set(leaf))

    if(len(parent) == 0):
        count = -1
        break
    count += 1

print(count)