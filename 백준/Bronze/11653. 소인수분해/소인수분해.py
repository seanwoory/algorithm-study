ip = int(input())
ans = ''

if ip == 1:
    pass

else:
    for i in range(2, ip + 1):
        if ip % i == 0:
            while ip % i == 0:
                ans = ans + str(i) + '\n'
                ip = ip // i
            if ip == 1:
                break
    print(ans)