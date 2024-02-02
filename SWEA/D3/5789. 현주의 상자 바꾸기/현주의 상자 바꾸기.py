T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    #N :현주가 가지고 있는 상자의 개수
    #Q :상자의 숫자를 변경하는 작업 횟수
    boxes = [0]*N

    for i in range(1, Q+1):
        Li, Ri = map(int, input().split())

        for j in range(Li-1, Ri):
            boxes[j] = i


    print(f'#{test_case}', *boxes)
