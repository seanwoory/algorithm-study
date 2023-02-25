st=input()
lst=['c=','c-','dz=','d-','lj','nj','s=','z=']
ans=0
N=len(st)
while True:
    for ch in lst:
        if ch in st:
            ans+=1
            st=st.replace(ch,' ',1)
            break
    else:
        break
st=st.strip()
while ' ' in st:
    st=st.replace(' ', '')
print(ans+len(st))