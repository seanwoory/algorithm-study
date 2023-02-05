T = int(input())
 
for test_case in range(1, T+1):
 
    n = int(input())
    cnt_lst = [0] * 100
    num_lst = list(map(int, input().split()))
    sorted_num_lst = [0] * n
    for num in num_lst:
        cnt_lst[num] += 1
 
    for idx in range(1, 100):
        cnt_lst[idx] += cnt_lst[idx-1]
 
    for num in num_lst:
        sorted_num_lst[cnt_lst[num] - 1] = num
        cnt_lst[num] -= 1
 
    print(f'#{test_case}', ' '.join(map(str,sorted_num_lst)))