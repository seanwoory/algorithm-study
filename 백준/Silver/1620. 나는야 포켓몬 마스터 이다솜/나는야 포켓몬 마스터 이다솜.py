import sys
input = sys.stdin.readline

n,m = map(int,input().split())

word_dic = {}
for i in range(1,n+1):
    word = input().strip()
    word_dic[word] = i
    word_dic[i] = word


for j in range(m):
    target = input().strip()

    if target.isdigit() == True:
        print(word_dic[int(target)])

    else:
        print(word_dic[target])