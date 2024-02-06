def sudoku(arr):
    for i in range(9):
        w = [0] * 10   #가로 검사
        h = [0] * 10   #세로 검사

        for j in range(9):
            w[arr[i][j]] += 1  # 가로 검사
            if w[arr[i][j]] == 2:
                return 0

            h[arr[j][i]] += 1    #세로 검사
            if h[arr[j][i]] == 2:
                return 0

    for i in range(0, 9, 3):       # 작은 스도쿠 검사
        for j in range(0, 9, 3):
            mini = [0] * 10
            for k in range(3):        # 작은 스도쿠의 크기만큼 반복
                for l in range(3):
                    # 가로검사
                    mini[arr[i+k][j+l]] += 1
                    if mini[arr[i+k][j+l]] == 2:
                        return 0

    return 1




T = int(input())

for test_case in range(1, T+ 1):
    tc = [list(map(int, input().split())) for _ in range(9)]

    result = sudoku(tc)

    print(f'#{test_case} {result}')