n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
s, e = min(arr) , max(arr)*m
ans = e

while s<=e:
    total = 0
    mid = (s+e)//2

    for i in range(n):
        total += mid//arr[i]

    if total >= m:
        e = mid - 1
        if ans > mid:
            ans = mid
    else:
        s = mid +1
print(ans)