import collections

n = int(input())
lst_n = list(map(int, input().split()))
cnt = collections.Counter()
for i in lst_n:
    cnt[i] += 1

m = int(input())
lst_m = list(map(int, input().split()))
ans = list()
for i in lst_m:
    ans.append(cnt[i])

print(*ans)