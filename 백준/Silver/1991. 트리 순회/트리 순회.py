import sys
from collections import defaultdict
 
N = int(sys.stdin.readline())

tree = defaultdict(list)
 
for n in range(N):
    parent, left_child, right_child = sys.stdin.readline().split()
    tree[parent] = [left_child, right_child]
 
 
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
 
 
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')
 
 
preorder('A')
print('')
inorder('A')
print('')
postorder('A')