def solution(fees, records):
    answer = []
    dct = {}
    for car in records:
        dct[car.split()[1]]=0
        
    for i in range(len(records)):
        lst = records[i].split()
        
        if lst[2]== 'IN':
            flag = True
            
            for j in range(i+1, len(records)):
                lst2 = records[j].split()
                if lst2[1]==lst[1] and lst2[2]=='OUT':
                    it = lst[0]
                    ot = lst2[0]
                    flag = False
                    break
                    
            if flag:
                it = lst[0]
                ot = "23:59"
            pay = 0
            if int(it[3:])==0: 
                hour = (int(ot[:2])-int(it[:2]))*60
                min = int(ot[3:])
            else:
                hour = (int(ot[:2]) - int(it[:2])) * 60 - 60
                min = int(ot[3:]) + int(60 - int(it[3:]))
            tm = hour + min
            dct[lst[1]] += tm
    ans = []
    
    for k,v in dct.items():
        pay = 0
        
        if v <= fees[0]:
            pay += fees[1]
        
        else:
            pay += fees[1]
            if (v - fees[0]) % fees[2]: 
                pay += ((v - fees[0]) // fees[2]+1)*fees[3]
            else:
                pay += ((v - fees[0]) // fees[2])*fees[3]

        ans.append([k,pay])
    ans.sort()
    
    for lst in ans:
        answer.append(lst[1])
    
    return answer