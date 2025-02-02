n = int(input())
lst = list(map(int, input().split()))
dp = [[1, [lst[i]]] for i in range(n)]
dp[0][1] = [lst[0]]
for i in range(1, n):
    for j in range(0, i):
        if lst[i] > lst[j]:
            if dp[j][0]+1 > dp[i][0]:
                dp[i][0] = dp[j][0]+1
                dp[i][1] = dp[j][1] + [lst[i]]

ans = max(dp)
print(ans[0])
print(*ans[1])