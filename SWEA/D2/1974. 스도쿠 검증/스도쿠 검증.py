T = int(input())

for test_case in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]   # 9x9 퍼즐
    result = 0  # 결과를 저장할 변수

    def puzzle_check():
        global result
        # 가로 한줄에 1-9까지의 숫자가 겹치지 않는지 확인
        for i in range(9):
            check = []  # 겹치는 숫자가 있는지 확인하기 위해 사용하는 리스트
            for j in range(9):
                if puzzle[i][j] not in check:
                    check.append(puzzle[i][j])
                else:   # 겹치는 숫자가 있을 경우
                    result = 0
                    return result

        # 세로 한줄에 1-9 까지의 숫자가 겹치지 않는지 확인
        for i in range(9):
            check = []  # 겹치는 숫자가 있는지 확인하기 위해 사용하는 리스트
            for j in range(9):
                if puzzle[j][i] not in check:
                    check.append(puzzle[j][i])
                else:
                    result = 0
                    return result


        # 작은 스도쿠 안에서 1-9까지의 숫자가 겹치지 않는지 확인
        for i in range(0, 6, 3):
            for j in range(0, 6, 3):
                check = []  # 겹치는 숫자가 있는지 확인하기 위해 사용하는 리스트
                for k in range(3):
                    for l in range(3):
                        if puzzle[i+k][j+l] not in check:
                            check.append(puzzle[i+k][j+l])
                        else:
                            result = 0
                            return result

        result = 1
        return result


    sol = puzzle_check()
    # 출력: 겹치는 숫자가 없을 경우 1, 겹칠 경우 0 출력
    print(f'#{test_case} {sol}')







