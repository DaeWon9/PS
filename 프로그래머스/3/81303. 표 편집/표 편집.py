class Node:
    def __init__(self, row_index):
        self.row_index = row_index
        self.next = None
        self.prev = None
        
root = Node(0)
node_size = 1

def add(current_node):
    global node_size

    new_node = Node(node_size)
    new_node.prev = current_node
    current_node.next = new_node
    node_size += 1
    return new_node
    
def add2(node):
    global root, node_size
    
    if (node.prev == None): # root
        root.prev = node
        root = node
        node_size += 1
        return
    
    if (node.next == None): # tail
        node.prev.next = node
        node_size += 1
        return
    
    node.prev.next = node
    node.next.prev = node
    node_size += 1
    return
    
def remove(target_node):
    global root, node_size
    
    if (target_node.prev == None): # root
        root.next.prev = None
        root = root.next
        node_size -= 1
        return root
            
    if (target_node.next == None): # tail
        target_node.prev.next = None
        node_size -= 1
        return target_node.prev


    prev_node = target_node.prev
    after_node = target_node.next

    prev_node.next = after_node
    after_node.prev = prev_node

    node_size -= 1
    
    return after_node
    
    
def solution(n, k, cmd):
    global root, node_size

    removed_list = []
    current_index = k
    current_node = root
    
    for _ in range(0, n-1):
        current_node = add(current_node)

    current_node = root
    for i in range(k):
        current_node = current_node.next
        
    for command in cmd:
        splited_command = command.split()
        if (splited_command[0] == 'D'):
            current_index += int(splited_command[1])
            if (current_index > node_size - 1):
                current_index = node_size - 1
                
            for _ in range(int(splited_command[1])):
                if (current_node.next != None):
                    current_node = current_node.next
                else:
                    break

        elif (splited_command[0] == 'U'):
            current_index -= int(splited_command[1])
            if (current_index < 0):
                current_index = 0
            for _ in range(int(splited_command[1])):
                if (current_node.prev != None):
                    current_node = current_node.prev
                else:
                    break
                
        elif (splited_command[0] == 'C'):
            removed_list.append(current_node)
            current_node = remove(current_node)
            if (current_index == node_size):
                current_index -= 1
            
        elif (splited_command[0] == 'Z'):
            node = removed_list.pop()
            add2(node)
            if (node.row_index <= current_index):
                current_index += 1
                
    result = ['O'] * n
    
    for node in removed_list:
        result[node.row_index] = 'X'
    
    answer = "".join(result)

    return answer