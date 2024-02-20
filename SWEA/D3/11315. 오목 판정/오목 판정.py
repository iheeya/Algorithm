T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    # o: 돌이 있는 칸, .: 돌이 없는 칸

    # 출력: 돌이 가로 , 세로, 대각선 중 하나의 방향으로 다섯개 이상 연속한 부분이 있는지
    # 있으면: YES, 없으면: NO 출력
    result = 'NO'  # 결과를 저장할 변수 result


    # 가로 오목
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(5):
                if 0<= j+k < N and arr[i][j+k] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = 'YES'

    # 세로 오목
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(5):
                if 0<= j+k < N and arr[j+k][i] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = 'YES'

    # 대각선 오목 (왼쪽 상단 -> 오른쪽 하단)
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(5):
                if 0<= j+k < N and 0<= i+k < N and arr[i+k][j+k] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = 'YES'

    # 대각선 오목( 오른쪽 상단 -> 왼쪽 하단)
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(5):
                if 0<= i+k < N and 0<= j-k < N and arr[i+k][j-k] == 'o':
                    cnt += 1
                    if cnt == 5:
                        result = 'YES'


    print(f'#{test_case} {result}')

