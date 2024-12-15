from collections import deque


def bfs(a, b):
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0]+i[0], v[1]+i[1]]
            if 0 <= nv[0] < n and 0 <= nv[1] < m:
                if lst[nv[0]][nv[1]] == '.':
                    lst[nv[0]][nv[1]] = 'D'
                elif not visit[nv[0]][nv[1]] and lst[nv[0]][nv[1]] == 'S':
                    visit[nv[0]][nv[1]] = 1
                    q.append(nv)
                elif lst[nv[0]][nv[1]] == 'W':
                    return False
    return True


def check():
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 'S':
                if not bfs(i, j):
                    print(0)
                    return
    print(1)
    for i in lst:
        print(''.join(i))


n, m = map(int, input().split())
visit = [[0 for _ in range(m)] for _ in range(n)]
lst = list(list(input()) for _ in range(n))
check()