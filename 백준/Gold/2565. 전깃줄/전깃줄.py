n = int(input())
visit = [0 for _ in range(501)]
mx = 0
for i in range(n):
    a, b = map(int, input().split())
    visit[a] = b
    if a > mx:
        mx = a

dp = [1 for _ in range(mx+1)]
for i in range(1, mx+1):
    if visit[i]:
        for j in range(1, i):
            if visit[j] and visit[i] > visit[j]:
                dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))