ip = int(input())
for _ in range(ip):
    n = int(input())
    lst = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[0] = lst[0]
    mx = dp[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1]+lst[i], lst[i])
        if dp[i] > mx:
            mx = dp[i]
    print(mx)