def stdev(tmp):
    mean = sum(tmp) / len(tmp)
    var = 0
    for num in tmp:
        var += (num - mean) ** 2
    var = var / len(tmp)
    sd = math.sqrt(var)
    return sd

import math
n, K = map(int, input().split())
lst = list(map(int, input().split()))
ans = 1e9
for i in range(n - K + 1):
    tmp = []
    for j in range(K):
        tmp.append(lst[i + j])
    sd = stdev(tmp)
    if ans > sd:
        ans = sd
    for k in range(i+j+1, n):
        tmp.append(lst[k])
        sd = stdev(tmp)
        if ans > sd:
            ans = sd
print(ans)