def dfs(x, y):
    global cnt  # 이동거리를 카운팅
    global visited

    # 기저조건: 상하좌우에 현재 값보다 1더 큰 수가 없다면 종료
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0<= nx< N and 0<= ny < N and (A[nx][ny] - A[x][y] == 1):
            cnt += 1
            dfs(nx, ny)

    return cnt



T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    room_num = float('inf')   # 이동거리가 큰 시작점중 가장 작은 수의 좌표를 저장할 변수

    result = 1   # 최대 이동 횟수를 저장할 변수

    dx = [0,  0, -1, 1]    # 델타 탐색을 위한 리스트
    dy = [1, -1, 0, 0]

    for i in range(N):
        for j in range(N):
            cnt = 1
            tmp = dfs(i, j)
            # 현재 자리에서 구한 이동 횟수가 최대 이동 횟수보다 크다면
            if tmp > 1:
                if tmp > result:
                    result = tmp
                    room_num = A[i][j]
                if tmp == result and (A[i][j] < room_num):
                    room_num = A[i][j]




    print(f'#{test_case} {room_num} {result}')

