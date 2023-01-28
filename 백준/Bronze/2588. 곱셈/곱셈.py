a = int(input())
b = str(input())
c = []
ans = 0

for num in b[-1:-4:-1]:
    c.append(int(num)*a)

for i in range(len(c)):
    print(c[i])
    ans += c[i] * 10 ** i

print(ans)
