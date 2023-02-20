pri = {'+':1, '-':1, '*':2, '/':2, '(':0}
st = input()

def back(st):
    stk = []
    ans = ''
    for ch in st:
        if ch.isalpha():
            ans+=ch
        else:
            if ch=='(':
                stk.append(ch)
            elif ch==')':
                while stk:
                    t=stk.pop()
                    if t=='(':
                        break
                    else:
                        ans+=t
            else:
                while stk and pri[ch]<=pri[stk[-1]]:
                    ans+=stk.pop()
                stk.append(ch)
    while stk:
        ans+=stk.pop()
    return ans
a = back(st)
print(a)