N, K = map(int,input().split())
lst= [(0,0)]
for _ in range(N):
    lst.append(tuple(map(int,input().split())))
dp = [[0]*(K+1) for _n in range(N+1)]

for i in range(1,N+1):
    for j in range(K+1):
        if lst[i][0] <= j :
            dp[i][j] = max(dp[i-1][j], lst[i][1], dp[i-1][j-lst[i][0]] + lst[i][1])  
        else: dp[i][j] = dp[i-1][j]


print(dp[N][K])