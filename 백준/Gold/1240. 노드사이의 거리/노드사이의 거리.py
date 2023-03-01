from collections import deque

def bfs(s,c):
    q = deque()
    q.append((s,0))
    v = [0] * (n+1)
    v[s] = 1
    while q:
        vert, d = q.popleft()
        if vert == c:
            return d
        for i, l in lst[vert]:
            if not v[i]:
                v[i] = 1
                q.append((i,d+l))
    
n, m = map(int,input().split())
lst = [[] for _ in range(n+1)]

for _ in range(n-1):
    n1, n2, l = map(int,input().split())
    lst[n1].append((n2,l))
    lst[n2].append((n1,l))

for _ in range(m):
    n1, n2 = map(int,input().split())
    print(bfs(n1,n2))