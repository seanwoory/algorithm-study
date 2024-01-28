import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(str(input().rstrip()))  

ans = set(lst) 
lst=list(ans) 
lst.sort()    
lst.sort(key=len)

for i in lst:
    print(i) 