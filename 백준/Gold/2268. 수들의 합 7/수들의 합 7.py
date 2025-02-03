import math
from sys import stdin, stdout


def update(left, right, node, idx, value):
    if left == right == idx:
        tree[node] = value
        return tree[node]
    if idx < left or right < idx:
        return tree[node]
    mid = (left + right) // 2
    tree[node] = update(left, mid, node*2, idx, value) + update(mid+1, right, node*2+1, idx, value)
    return tree[node]


def calc(left, right, node, lidx, ridx):
    global sm
    if lidx <= left <= ridx and lidx <= right <= ridx:
        sm += tree[node]
        return
    if right < lidx or ridx < left:
        return
    mid = (left + right) // 2
    calc(left, mid, node*2, lidx, ridx)
    calc(mid+1, right, node*2+1, lidx, ridx)


n, m = map(int, stdin.readline().split())
tree = [0 for _ in range(2**math.ceil(math.log2(n)+1))]
for i in range(m):
    a, b, c = map(int, stdin.readline().split())
    if a:
        update(1, n, 1, b, c)
    else:
        b, c = min(b, c), max(b, c)
        sm = 0
        calc(1, n, 1, b, c)
        stdout.write(str(sm) + '\n')