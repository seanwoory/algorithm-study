T = int(input())
for test_case in range(1, T + 1):
    mat_lst = []

    for i in range(9):
        mat_lst.append(list(map(int, input().split())))

    def factorial(n):
        result = 1
        for i in range(1, 1+n):
            result *= i
        return result
    
    def row(mat):
        flag = True
        for lst in mat:
            cert = 1
            for i in range(len(lst)):
                cert *= lst[i]
            if cert == factorial(9):
                flag = True
            else:
                flag = False
                break
        return flag
    
    def col(mat):
        flag = False
        for i in range(len(mat)):
            cert = 1
            for j in range(len(mat)):
                cert *= mat[j][i]
            if cert == factorial(9):
                flag = True
            else:
                flag = False
                break
        return flag

    def nine(mat):
        for _ in range(3):
            temp_mat = []
            for i in range(3):                
                temp_mat.append(mat.pop(0))                
                if i == 2 or i == 5 or i == 8:
                    for _ in range(3):
                        cert = 1
                        for k in range(3):
                            for _ in range(3):
                                cert *= temp_mat[k].pop(0)
                        if cert == factorial(9):
                            return True
                        else:
                            return False                       
    flag_ovr = 0
    if (row(mat_lst) == True) and (col(mat_lst) == True) and (nine(mat_lst) == True):
        flag_ovr = 1

    print(f'#{test_case} {flag_ovr}')