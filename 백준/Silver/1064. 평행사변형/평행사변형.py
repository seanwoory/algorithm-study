ip = list(map(int, input().split()))

a = ip[0:2]
b = ip[2:4]
c = ip[4:]
ans_lst = []
ab = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)
ac = ((a[0]-c[0])**2 + (a[1]-c[1])**2)**(1/2)
bc = ((c[0]-b[0])**2 + (c[1]-b[1])**2)**(1/2)

if a[0] == b[0] == c[0]:
    print('-1.0')

elif a[1] == b[1] == c[1]:
    print('-1.0')

else:
    if (a[1]-b[1]) != 0 and (c[1]-b[1]) != 0:
        if ((a[0] - b[0]) / (a[1] - b[1])) == ((c[0] - b[0]) / (c[1] - b[1])):
            print('-1.0')

        else:
            ans_lst.append(ab + ac)
            ans_lst.append(ab + bc)
            ans_lst.append(ac + bc)
            ans_lst.sort()
            print((ans_lst[-1] - ans_lst[0]) * 2)

    else:
        ans_lst.append(ab + ac)
        ans_lst.append(ab + bc)
        ans_lst.append(ac + bc)
        ans_lst.sort()
        print((ans_lst[-1] - ans_lst[0]) * 2)