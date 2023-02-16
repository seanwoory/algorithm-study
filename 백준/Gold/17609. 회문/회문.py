def isPal(st):
    # 유사 회문을 거르는 함수를 작성함.
    # 문자 하나씩 검사해서 같으면 pass, 아니면 유사회문인지 판단.
    # 왼쪽 문자와 오른쪽 문자의 인덱스를 가리킴.
    # xabba
    l=0
    r=len(st)-1

    # 반만 돌고 싶어서, l<r
    while l<r:
        # left right 문자가 동일할 경우, left +1, right -1
        # 왼쪽 문자와 오른쪽 문자가 같다면, left right 인덱스를 하나씩 옮기고 pass.
        if st[l]==st[r]:
            l += 1
            r -= 1
        else:
            # 2. left right 문자가 다른 경우,
            # 둘중 어떤 문자를 지워야지 회문이 되는지 알 수 없음.
            # 먼저, 오른쪽 문자열 제거한 경우 제거 후 회문이 되는지 확인
            if l<=r-1:
                # st[r]을 제외한 문자열을 temp에 저장.
                # 이후 temp를 뒤집어 원래 순서와 동일하다면 return 1.
                temp = st[:r] + st[r+1:]
                if temp[:]==temp[::-1]:
                    return 1
            # 이후, 왼쪽 문자열 제거 후 회문이 되는지 확인
            elif l+1<=r:
                # 오른쪽과 동일한 논리로 확인.
                temp = st[:l]+st[l+1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2


T = int(input())
for _ in range(T):
    # str 자료형으로 input을 받음.
    st = input()
    # 회문이라면, print(0)
    # comwwmoc
    if st==st[::-1]:
        print(0)
    else:
        print(isPal(st))