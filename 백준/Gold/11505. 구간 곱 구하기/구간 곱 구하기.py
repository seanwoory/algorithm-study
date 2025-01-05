import math
from sys import stdin, stdout

def init(left, right, node):
    if left == right:
        tree[node] = lst[left-1]
        return tree[node]
    mid = (left + right) // 2
    tree[node] = (init(left, mid, node*2) * init(mid+1, right, node*2+1)) % 1000000007
    return tree[node]


def update(left, right, node, idx, value):
    if left == right == idx:
        tree[node] = value
        return
    if idx < left or right < idx:
        return
    mid = (left + right) // 2
    update(left, mid, node*2, idx, value)
    update(mid+1, right, node*2+1, idx, value)
    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007


def find(left, right, node, lidx, ridx):
    global ans
    if ridx < left or right < lidx:
        return
    elif lidx <= right <= ridx and lidx <= left <= ridx:
        ans = (ans * tree[node]) % 1000000007
        return
    mid = (left + right) // 2
    find(left, mid, node*2, lidx, ridx)
    find(mid+1, right, node*2+1, lidx, ridx)


n, m, k = map(int, stdin.readline().split())
lst = list(int(stdin.readline()) for _ in range(n))
tree = [1 for _ in range(2**(math.ceil(math.log2(n)+1)))]
init(1, n, 1)
for i in range(m+k):
    a, b, c = map(int, stdin.readline().split())
    if a == 1:
        update(1, n, 1, b, c)
    else:
        ans = 1
        find(1, n, 1, b, c)
        stdout.write(str(ans) + '\n')