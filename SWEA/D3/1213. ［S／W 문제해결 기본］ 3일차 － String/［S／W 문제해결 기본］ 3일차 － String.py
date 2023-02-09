T = 10
for tc in range(1, 1+T):
    _ = input()
    a = input()
    b = input()
    ans = 0

    for i in range(len(b)-len(a)+1):
        if a in b[i:i+len(a)]:
            ans += 1


    print(f'#{tc} {ans}')
