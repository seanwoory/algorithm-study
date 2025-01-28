n = int(input())
now, cnt, d = 1, 2, 1
lst = []
while d <= n:
    if d != 1:
        lst.append(d)
    now += cnt
    cnt += 1
    d += now
dp = [i for i in range(n+1)]
dp[0] = 0
for i in lst:
    for j in range(i, n+1):
        dp[j] = min(dp[j-i]+1, dp[j])
print(dp[n])