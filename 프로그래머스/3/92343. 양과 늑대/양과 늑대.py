left_child = [-1] * 20
right_child = [-1] * 20
values = []
node_count = 0
max_sheep = 1
visited = [0] * (1 << 17)

def explore(state):
    global max_sheep
    if (visited[state]):
        return
    visited[state] = 1

    wolf_count, total_nodes = 0, 0
    for i in range(node_count):
        if (state & (1 << i)):
            total_nodes += 1
            wolf_count += values[i]

    if (2 * wolf_count >= total_nodes):
        return

    max_sheep = max(max_sheep, total_nodes - wolf_count)

    for i in range(node_count):
        if (not (state & (1 << i))):
            continue
        if (left_child[i] != -1):
            explore(state | (1 << left_child[i]))
        if (right_child[i] != -1):
            explore(state | (1 << right_child[i]))

def solution(info, edges):
    global node_count, values
    node_count = len(info)
    values = info[:]
    for u, v in edges:
        if (left_child[u] == -1):
            left_child[u] = v
        else:
            right_child[u] = v

    explore(1)
    return max_sheep
