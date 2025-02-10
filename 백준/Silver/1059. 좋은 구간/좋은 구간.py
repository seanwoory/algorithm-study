l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()
min = 1
max = 1000
for i in s:
    if n > i:
        min = i + 1

    if n < i:
        max = i - 1
        break

if n == min:
    ans = max - n

else:
    ans = (n - min + 1) * (max - n + 1) - 1

if n in s:
    ans = 0

print(ans)