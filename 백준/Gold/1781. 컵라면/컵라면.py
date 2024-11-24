import heapq
from sys import stdin, stdout
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        root[b] = a
    else:
        root[a] = b
def find(a):
    if a == root[a]:
        return a
    root[a] = find(root[a])
    return root[a]
n = int(stdin.readline())
heap = []
N = 0
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    heapq.heappush(heap, [-b, b, a])
    if N < a:
        N = a
lst = [0 for _ in range(N+1)]
root = [i for i in range(N+1)]
for _ in range(n):
    t = heapq.heappop(heap)
    idx = find(t[2])
    if idx > 0:
        lst[idx] = t[1]
        union(idx, idx-1)

print(sum(lst))