N, L = map(int, input().split())
pos = 0
ans = 0

for _ in range(N):
    d, r, g = map(int, input().split())

    ans += (d - pos)
    pos = d
    if ans % (r+g) <= r:
        ans += (r - (ans%(r+g)))

ans += (L-pos)
print(ans)