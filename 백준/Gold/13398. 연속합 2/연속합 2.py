n = int(input())
lst = list(map(int, input().split()))
mx = -1000
dp = [[-1000 for _ in range(n)] for _ in range(2)]
for i in range(n):
    dp[0][i] = max(dp[0][i-1]+lst[i], lst[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + lst[i])
    mx = max(mx, dp[0][i], dp[1][i])
print(mx)