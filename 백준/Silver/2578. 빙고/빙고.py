def check1():
    # 빙고인지 알아보기 (가로)
    binggo_cnt = 0
    for i in range(5):
        cnt = 0   # 빙고인지 카운트
        for j in range(5):
            if bingo[i][j] == 0:
                cnt += 1
        if cnt == 5:
            binggo_cnt += 1
    
    return binggo_cnt

def check2():
    # 빙고인지 알아보기 (세로)
    binggo_cnt = 0
    for i in range(5):
        cnt = 0   # 빙고인지 카운트
        for j in range(5):
            if bingo[j][i] == 0:
                cnt += 1
        if cnt == 5:
            binggo_cnt += 1

    return binggo_cnt

def check3():
    binggo_cnt = 0
    cnt = 0   # 빙고인지 카운트
    # 빙고인지 알아보기 (대각선1)
    for i in range(5):
        if bingo[i][i] == 0:
            cnt += 1
        if cnt == 5:
            binggo_cnt += 1
    return binggo_cnt

def check4():
    binggo_cnt = 0
    # 빙고인지 알아보기 (대각선2)
    cnt = 0   # 빙고인지 카운트
    for i in range(5):
        if bingo[i][4-i] == 0:
            cnt += 1
        if cnt == 5:
            binggo_cnt += 1
    
    return binggo_cnt




bingo = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]  # 사회자가 부르는 수
result = 0   # 사회자가 몇번째 수를 부른후 빙고를 외치게 될지 저장할 변수

for num in arr:
    for n in num:
        result += 1 
        # 빙고 개수가 3 이상이면 출력
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == n:
                    bingo[i][j] = 0
                    # 빙고 표시하기
        
        if check1() + check2() + check3() + check4() >= 3:
            print(result)
            break
    
    if check1()+ check2() + check3() + check4() >= 3:
        break
    
        


       