s=[]
x=[]
y=[]
ln=[]

k=int(input())

for i in range(6):
    w,d=map(int, input().split())
    s.append([w,d])
    if s[i][0]==3 or s[i][0]==4:
        x.append(s[i][1])
    if s[i][0]==1 or s[i][0]==2:
        y.append(s[i][1])

for i in range(6):
    if s[i][0]==s[(i+2)%6][0]:
        ln.append(s[(i+1)%6][1])
print(((max(x)*max(y))-(ln[0]*ln[1]))*k)