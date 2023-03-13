def solution(cap, n, deliveries, pickups):
    distance = 0  # 최종 거리
    remain_deliver = 0
    remain_pickup = 0
    for i in range(n - 1, -1, -1):  # 가장 먼 집부터 정복
        remain_deliver += deliveries[i]  # 현재 보고 있는 집 까지의 남은 배달 수, 양수로 관리
        remain_pickup -= pickups[i]  # 현재 보고 있는 집 까지의 남은 수거 수, 음수로 관리

        deliver_cnt = 0
        pickup_cnt = 0
        temp_deliver = remain_deliver  # deliver count 체크를 위한 임시 remain_deliver
        temp_pickup = remain_pickup  # pickup count 체크를 위한 임시 remain_pickup
        # 현재 보고 있는 집의 task 가 소진 되기 까지의 과정, 0 기준 조건 만족 (소진)
        while True:
            if temp_deliver <= 0:
                break
            temp_deliver -= cap
            deliver_cnt += 1
        while True:
            if temp_pickup >= 0:
                break
            temp_pickup += cap
            pickup_cnt += 1

        # cnt: 처리 해야 하는 남은 물품 없이 다녀 와야 하는 횟수, 둘 중 더 큰 수로 결정
        cnt = max(deliver_cnt, pickup_cnt)
        remain_deliver -= cnt * cap
        remain_pickup += cnt * cap
        distance += (i + 1) * cnt * 2  # 거리 더하기 (왕복)
    return distance