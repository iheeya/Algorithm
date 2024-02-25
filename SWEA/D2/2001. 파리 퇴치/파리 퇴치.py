
T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    # N: 배열의 길이, M: 파리채의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    mx = 0  # 가장 많이 죽인 파리의 수


    # 파리채를 통해 가장 많이 죽은 파리는?
    for i in range(N-M+1):   # 파리채가 이동할 수 있는 시작지점만큼 반복
        for j in range(N-M + 1):
            cnt = 0  #죽인 파리의 개수
            for k in range(i, M+i):
                for l in range(j, M+j):
                    cnt += arr[k][l]
            
            if cnt > mx:
                mx = cnt

    print(f'#{test_case} {mx}')            
