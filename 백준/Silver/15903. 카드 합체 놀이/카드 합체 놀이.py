N, T = map(int,input().split())
lst = list(map(int,input().split()))


for _ in range(T):
    lst.sort()
    lst[0] = lst[1] = lst[0]+lst[1]

print(sum(lst))