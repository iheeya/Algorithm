def move(cnt, x, y, g):
    global result, room_num, sol, z, q
    # 상하좌우에 있는 다른 방으로 이동 가능
    # 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
    price = arr[x][y]  # 현재 위치의 값

    g.append((x, y))
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == price + 1:  # 한칸 이동한 위치의 값이 현재 값보다 1더 크다면
                move(cnt + 1, nx, ny, g)

    # 상하좌우를 모두 탐색했음에도 이동할 위치가 없다면
    else:  # 기저조건: 현재 있는 방의 상하좌우의 값 중에 1더 큰 숫자가 없으면 종료
        result = cnt
        if result == sol:    # 이동한 거리가 같을 경우
            sol = result
            z, q = g[0]
            if arr[z][q] < room_num:    # 더 작은 방을 값을 출력
                room_num = arr[z][q]
        elif result > sol:   # 이동한 거리가 더 멀 경우
            sol = result
            z, q = g[0]
            room_num = arr[z][q]   # 새로운 방 번호 지정

        return



T = int(input())

for test_case in range(1, T+1):
    N = int(input())   # 2차원 배열의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    room_num = 1000000  # 방 번호
    # (만약 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은것 출력)
    sol = 0 # 가장 작은 수를 가진 방을 저장할 변수
    z = 0   # arr의 x좌표
    q = 0   # arr의 y좌표

    dx = [0, 0, -1, 1]    # 상하좌우로 이동할 인덱스
    dy = [1, -1, 0, 0]

    result = 0  # 이동한 거리를 저장할 변수

    # 처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있을까? -> 모든 경우 탐색
    for i in range(N):
        for j in range(N):
            move(1, i, j, [])


    # TODO: 메모이제이션을 활용해 재귀가 너무 많이 돌지 않도록
    # 출력: 처음에 출발해야 하는 방 번호, 최대 몇 개의 방으로 이동가능한지
    print(f'#{test_case} {room_num} {sol}')
