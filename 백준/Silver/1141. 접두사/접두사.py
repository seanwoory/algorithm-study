ip = int(input())
lst = list()

for i in range(ip):
    dummy = input()
    if dummy in lst:
        continue

    lst.append(dummy)

ans_lst = lst[:]

for i in lst:
    for j in lst:
        if i == j:
            continue

        else:
            if i == j[:len(i)]:
                if i in ans_lst:
                    ans_lst.remove(i)

print(len(ans_lst))