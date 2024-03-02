switch_num = int(input())   # 스위치 개수
switch = list(map(int, input().split()))   # 스위치 상태
student_num = int(input())   # 학생수

for _ in range(student_num):
    sex, num = map(int, input().split())   # 성별, 받은 수

    if sex == 1:   # 성별이 남자라면
       for i in range(num, switch_num+1, num):
            if switch[i-1] == 1:
                switch[i-1] = 0
            else:
                switch[i-1] = 1
            
   

       
    
    elif sex == 2:
        num = num -1    # 배열의 인덱스는 0부터 시작하므로 넘버값하나 줄이기
        if switch[num] == 0:
            switch[num] = 1
        else:
            switch[num] = 0
        
        for i in range(1, switch_num):
            if 0<= num-i and num + i < switch_num:
                if switch[num - i] == switch[num + i]:   # 서로 대칭인 수가 같다면
                    if switch[num -i] == 0:
                        switch[num - i] = 1
                        switch[num + i] = 1
                    else:
                        switch[num - i] = 0
                        switch[num + i] = 0
                else:
                    break
            else:
                break
        


# 한줄에 20개씩 출력
for i in range(0, len(switch), 20):
    print(*switch[i:i+20])
        