T = 10
n = 100
for tc in range(1, T + 1):
    t_n = int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]
 
    r = 99
    c = -1
		# 거꾸로 올라가기 위한 도착지점 찾기
    for i in range(n):
        if ladders[r][i] == 2:
            c = i
 
    dr = [0, 0, -1]
    dc = [-1, 1, 0]
		# 도착지점으로부터 역으로 올라가되, 지나갔던 지역을 가지 않도록 다리 없애는 과정 진행
    while r > 0:
 
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nc < n and 0 <= nr < n and ladders[nr][nc] == 1:
                r = nr
                c = nc
                ladders[r][c] = 0
                break
 
    print(f"#{tc} {c}")