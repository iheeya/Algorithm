T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    # N: 퍼즐의 판 길이
    # K: 단어의 길이

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # K길이의 단어가 들어갈 수 있는 칸의 수

    # 가로 단어
    for i in range(N):
        cnt = 0   # 문자가 들어갈 수 있는 칸의 수
        for j in range(N):
            if puzzle[i][j] == 1:
                # 1: 단어가 들어갈 수 있음  0: 단어가 들어갈 수 없음
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                if puzzle[i][j] == 0:
                    cnt = 0

    # 세로 단어
    for i in range(N):
        cnt = 0  # 문자가 들어갈 수 있는 칸의 수
        for j in range(N):
            if puzzle[j][i] == 1:
                # 1: 단어가 들어갈 수 있음  0: 단어가 들어갈 수 없음
                cnt += 1
            if puzzle[j][i] == 0 or j == N - 1:
                if cnt == K:
                    result += 1
                if puzzle[j][i] == 0:
                    cnt = 0

    print(f'#{test_case} {result}')
