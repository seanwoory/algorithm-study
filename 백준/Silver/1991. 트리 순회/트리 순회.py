N = int(input())
lst = {}
 
for n in range(1,N+1):
    root, left, right = map(str,input().split())
    lst[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')  
        preorder(lst[root][0])
        preorder(lst[root][1])
 
 
def inorder(root):
    if root != '.':
        inorder(lst[root][0])
        print(root, end='') 
        inorder(lst[root][1])
 
 
def postorder(root):
    if root != '.':
        postorder(lst[root][0])
        postorder(lst[root][1])
        print(root, end='')
 
 
preorder('A')
print()
inorder('A')
print()
postorder('A')