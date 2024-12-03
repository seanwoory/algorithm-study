from sys import stdin
from collections import deque


def bfs(i):
    q = deque()
    q.append(i)
    visit[i] = 1
    while q:
        v = q.popleft()
        for i in lst[v]:
            if not visit[i]:
                q.append(i)
                visit[i] = 2 - visit[v] + 1
            else:
                if visit[i] == visit[v]:
                    return 'NO'
    return 'YES'


ip = int(stdin.readline())

for _ in range(ip):
    n, m = map(int, stdin.readline().split())
    lst = [[] for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    visit[0] = 1
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        lst[a].append(b)
        lst[b].append(a)

    for i in range(1, n+1):
        if lst[i] and not visit[i]:
            ans = bfs(i)
            if ans == 'NO':
                print(ans)
                break
    else:
        print(ans)