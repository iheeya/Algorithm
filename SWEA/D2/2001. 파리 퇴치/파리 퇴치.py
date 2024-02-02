T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())   # N: 배열의 크기  M: 파리채의 크기
    my_matrix = [list(map(int, input().split())) for _ in range(N)]
    
    max = 0   #최대값
    
    for row in range(N-M+1):      #확인해야 할 개수의 시작 좌표
        for col in range(N-M+1):
            cnt = 0     # 파리채로 죽인 파리의 개수를 저장할 변수
            for x in range(row, row+M):   #시작좌표에서 부터 파리채의 크기만큼
                for y in range(col, col+M):
                    cnt += my_matrix[x][y]   # 파리채의 크기 안에서 죽은 파리의 개수
                    
            if cnt > max:
                max = cnt
                
    print(f'#{test_case} {max}')
