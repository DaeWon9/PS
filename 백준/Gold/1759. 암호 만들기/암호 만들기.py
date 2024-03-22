import sys
input = sys.stdin.readline

def is_password(target):
    m_count = 0
    j_count = 0
    for s in target:
        if s in moeum:
            m_count += 1
        else:
            j_count += 1
    if (m_count >= 1 and j_count >= 2):
        return True
    return False

moeum = {'a', 'e', 'i', 'o', 'u'}

def dfs(target : list):
    if (len(target) == L):
        if (is_password(target)):
            print("".join(target))
            return
    
    for alphabet in alphabet_list:
        if alphabet > target[-1]: # 사전순
            target.append(alphabet)
            dfs(target)
            target.pop()

L, C = map(int, input().split())
alphabet_list = list(input().split())
alphabet_list.sort()

for i in range(C - L + 1):
    dfs([alphabet_list[i]])