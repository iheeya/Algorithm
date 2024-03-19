T = int(input())

# 6번 이동한 칸의 숫자를 이어붙여 7자리의 숫자가 되도록 한다. (완전탐색을 통해 모든 경우의 수 탐색)
def make_nums(level, x, y):
    global idx
    global lst

    # 기저조건: 이동 횟수가 6번이 되면 종료
    if level == 7:   # 시작 위치도 랜덤으로 정해야 한다.
        # make_nums 의 반환 값을 집합 A에 넣기 (집합에 넣어서 중복 제거)
        A.add(''.join(map(str, lst))) # 7개의 숫자가 저장된 리스트를 하나의 순자로 바꾼다.
        return

    #  격자판 안에 있는 범위일때만 이동

    for j in range(4):
        nx = dx[j] + x
        ny = dy[j] + y
        if 0<= nx < 4 and 0<= ny <4:
            lst[level] = arr[nx][ny]  # 결정
            make_nums(level+1, nx, ny)
            lst[level] = 0  # 복구


for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]  # 격자판
    # 상하좌우로 중 하나로 총 여섯번 이동
    # 상하좌우 이동을 위한 델타 리스트
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    idx = 1

    A = set()  # 겹치지 않는 숫자들을 저장할 집합
    lst = [0] * 7   # 방문한 숫자를 넣을 리스트

    for i in range(4):   # 모든 경우의 시작점 구하기
        for j in range(4):
            lst[0] = arr[i][j]
            make_nums(1, i, j)


    # 출력: 만들 수 있는 서로 다른 일곱 자리 수들의 개수
    print(f'#{test_case} {len(A)}')