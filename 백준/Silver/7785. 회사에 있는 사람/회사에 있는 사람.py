from sys import stdin, stdout

n = int(stdin.readline());
now = {}

for i in range(n):
    a, b = map(str, stdin.readline().split())
    if b == 'enter':
        now[a] = 1
    else:
        now[a] = 0

ans = []
for i in now:
    if now[i]:
        ans.append(i)

ans.sort(reverse=True)
for i in ans:
    stdout.write(i + '\n')