for test_case in range(1, 11):
    T = int(input())
    my_matrix = [list(map(int, input().split())) for _ in range(100)]

    mx = 0    #각 행, 열 대각선의 합 중 최대값을 저장할 변수

    for row in range(100):    # 행의 합
        cnt = 0   # 한 줄의 합을 저장할 변수
        for col in range(100):
            cnt += my_matrix[row][col]
        
        if mx < cnt:
            mx = cnt

    
    for row in range(100):   #열의 합
        cnt = 0
        for col in range(100):
            cnt += my_matrix[col][row]
        
        if mx < cnt:
            mx = cnt


    for row in range(10):   # 대각선(좌측 상단 -> 우측 하단)
        cnt = 0 
        cnt += my_matrix[row][row]

    if mx < cnt:
        mx = cnt


    for row in range(9, -1, -1):   # 대각선 (우측 상단 -> 좌측 하단)
        cnt = 0
        for col in range(10):
            cnt += my_matrix[row][col]
        
        if mx < cnt:
            mx = cnt

    print(f'#{test_case} {mx}')