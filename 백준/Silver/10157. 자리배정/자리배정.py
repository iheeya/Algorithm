def func(x, y):
    global seat
    dy = [0, 1, 0, -1]    # 4방향(문제와는 배열 뒤집어서 보기)
    dx = [1, 0, -1, 0]    
    idx =  0  # 인덱스
    tmp = 1
    while tmp != K:
        seat[x][y] = 1   # 현재 좌표에 1 표시

        nx = x + dx[idx]  # 다음 좌표 구하기
        ny = y + dy[idx]
        
        if 0<= nx < R and 0<= ny < C and seat[nx][ny] == 0:   # 다음 좌표가 범위 내에 있다면
            x, y = nx, ny   # 현재좌표로 만들기
            tmp += 1
        else:    # 범위 안에 없으면
            idx = (idx + 1) % 4    # 다음 4방향 탐색
    
    return  y+1, x + 1   # dx, dy를 배열과는 다른방향으로 구했으므로 순서 바꾸기




C, R = map(int, input().split())   # 가로, 세로 길이
K = int(input())   # 관객 번호
seat = [[0] * C for _ in range(R)]

if K> C*R:
    print(0)   # 관객번호가 배여ㄹ보다 크면 0 출력
else:
    print(*func(0, 0))    # 배열 뒤집어서 보기

