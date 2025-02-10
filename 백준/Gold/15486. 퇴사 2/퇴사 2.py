from sys import stdin


n = int(stdin.readline())
dp = [0 for _ in range(n)]
for i in range(n):
    a, b = map(int, stdin.readline().split())
    dp[i] = max(dp[i], dp[i-1])
    if a+i-1 > n-1:
        continue
    dp[a+i-1] = max(dp[i-1] + b, dp[a+i-1])
print(dp[n-1])