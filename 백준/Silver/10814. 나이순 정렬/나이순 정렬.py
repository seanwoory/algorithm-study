N = int(input())
lst = []
for _ in range(N):
    age, name = map(str,input().split())
    lst.append((int(age), name))

for i in sorted(lst, key=lambda x:x[0]):
    print(*i) 