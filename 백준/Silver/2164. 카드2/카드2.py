from collections import deque

N = int(input())
card = deque()

for i in range(1, N+1): #큐 생성
    card.append(i)
while len(card)>1: #조건문 실행
    card.popleft()
    a = card.popleft()
    card.append(a)

print(card[0])