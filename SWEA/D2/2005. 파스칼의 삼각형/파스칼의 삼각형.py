# 파스칼의 삼각형

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            if i== j or j == 0:   # 시작과 끝은 1
                arr[i][j] = 1
            # 중간 합계 구하기
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{test_case}')
    for row in arr:
        result = []   # 파스칼의 삼각형을 출력할 배열
        for x in row:
            if x :    # x가 값이 있다면
                result += [x]

        print(*result)


