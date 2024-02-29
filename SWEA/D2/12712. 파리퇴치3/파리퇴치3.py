T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N: 파리가 있는 공간의 크기  M: 파리를 잡을 수 있는 칸 수
    flys = [list(map(int, input().split())) for _ in range(N)]
    mx = 0   # 가장 많이 잡은 파리 수를 저장할 변수

    # 노즐이 +, x 형태로 분사 (뿌려진 일부가 영역을 벗어나도 괜찮다.)

    # + 형태를 탐색할 델타탐색
    for i in range(N):
        for j in range(N):
            cnt = 0   # 한번에 잡은 파리수
            cnt += flys[i][j]  # 자기자신 더하기
            for n in range(1, M):
                dx_1 = [n, -n, 0, 0]
                dy_2 = [0, 0, -n, n]
                for k in range(4):
                    nx = dx_1[k] + i
                    ny = dy_2[k] + j
                    if 0 <= nx <N and 0<= ny<N:
                        cnt += flys[nx][ny]

            if cnt > mx:
                mx = cnt


    # x 형태를 탐색할 델타 탐색
    for i in range(N):
        for j in range(N):
            cnt = 0   # 한번에 잡은 파리수
            cnt += flys[i][j]  # 자기자신 더하기
            for n in range(1, M):
                dx = [-n, -n, n, n]   # x자 형태로 탐색할 델타탐색 배열만들기
                dy = [-n, n, n, -n]
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx <N and 0<= ny<N:
                        cnt += flys[nx][ny]

            if cnt > mx:
                mx = cnt

    print(f'#{test_case} {mx}')