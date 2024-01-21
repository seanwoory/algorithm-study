import sys
input = sys.stdin.readline

lst = []
n,k = map(int,input().split())
for _ in range(n):
    lst.append(int(input().strip()))

cnt = 0
lst.sort(reverse=True)

for i in lst:
    if i <= k:
        cnt += k // i
        k = k%i
        if k == 0:
            break
print(cnt) 