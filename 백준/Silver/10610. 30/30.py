n = list(input())
n.sort(reverse=True)
total = 0
ans = False
for i in n:
    if i == '0':
        ans = True
    total = total + int(i)

if ans:
    if total % 3 == 0:
        print(''.join(n))
    else:
        print(-1)
else:
    print(-1)