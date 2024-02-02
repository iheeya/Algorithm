T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # N: 행   M: 열
    flower = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 배열의 처음부터 끝까지 순회하면서 본인, 상하좌우의 합을 구해서
    # 리스트에 그 값을 넣는다
    # (이때 상하좌우 중 좌표가 존재하지 않는 곳이 있다면 0을 더하거나 무시)

    # 2차원 배열의 순회를 마치면 배열에 저장된 가장 큰 값을 출력

    max_flower = []

    for i in range(N):
        for j in range(M):
            total = 0
            num = flower[i][j]   #본인 숫자 num에 저장. 이 num 길이만큼 상하좌우의 풍선 터뜨리기

            for n in range(1, num + 1):
                di = [0, n, 0, -n]  # 주변을 탐색하기 위한 좌표 계산값
                dj = [n, 0, -n, 0]
                for k in range(4):  # 탐색할 4개의 칸에 대해
                    ni = i + di[k]  # 탐색하고자 하는 좌표로 가기
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:  # 좌표 범위 안에 있을때만 배열에 접근하도록 한다.
                        total += flower[ni][nj]

            total += flower[i][j]  # 본인 숫자도 더하기
            max_flower.append(total)  # 계산 결과 저장

    print(f'#{test_case} {max(max_flower)}')