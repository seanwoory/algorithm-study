import sys
input = sys.stdin.readline

arr = {}
n,m = map(int,input().split())

lst = []
for _ in range(n):
    lst.append(input().split())

for site, bi in lst:
    arr[site] = bi

ans = []
for i in range(m):
    target = input().strip()

    if target in arr:
        ans.append(arr[target])

for i in ans:
    print(i) 