from collections import deque
import copy


def bfs(a, b, tmp):
    way = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([a, b])
    visit[a][b] = 1
    while q:
        v = q.popleft()
        for i in way:
            nv = [v[0] + i[0], v[1] + i[1]]
            if 0 <= nv[0] <= n-1 and 0 <= nv[1] <= m-1 and not visit[nv[0]][nv[1]] and not tmp[nv[0]][nv[1]]:
                q.append(nv)
                visit[nv[0]][nv[1]] = 1
                tmp[nv[0]][nv[1]] = 2


def wall(cnt):
    global visit, mx
    if cnt == 3:
        ans = 0
        visit = [[0 for _ in range(m)] for _ in range(n)]
        tmp = copy.deepcopy(lst)
        for i in range(n):
            for j in range(m):
                if lst[i][j] == 2:
                    bfs(i, j, tmp)
        for i in range(n):
            for j in range(m):
                if not tmp[i][j]:
                    ans += 1
                    if ans > mx:
                        mx = ans
        return

    for i in range(0, n):
        for j in range(0, m):
            if lst[i][j] == 0:
                lst[i][j] = 1
                wall(cnt + 1)
                lst[i][j] = 0


n, m = map(int, input().split())
lst = list(list(map(int, input().split())) for _ in range(n))
visit = [[0 for _ in range(m)] for _ in range(n)]
mx = 0
wall(0)
print(mx)