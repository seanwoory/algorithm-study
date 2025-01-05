def dfs(a, cnt):
    global ans, d
    if cnt == n-1:
        if lst[a][0]:
            d += lst[a][0]
            if d < ans:
                ans = d
            d -= lst[a][0]
            return

    for i in range(n):
        if not visit[i] and lst[a][i]:
            visit[i] = 1
            d += lst[a][i]
            dfs(i, cnt+1)
            d -= lst[a][i]
            visit[i] = 0


n = int(input())
lst = list(list(map(int, input().split())) for _ in range(n))
visit = [0 for _ in range(n)]
ans = 10**7
d = 0
visit[0] = 1
dfs(0, 0)
print(ans)