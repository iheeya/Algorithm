T = int(input())

for test_case in range(1, T+1):
    N, B = map(int, input().split())  #N: 직원 수, B: 선반의 높이
    S = list(map(int, input().split()))  # 각 점원의 키
    tower_h = 0  # 탑의 높이
    result = 1000000 # 제일 낮은 탑의 높이

    # 탑의 높이가 B이상인 경우 선반 위의 물건을 사용할 수 있다.

    # 비트연산자를 이용해 부분집합 만들기
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(S[j])

        if sum(subset) >= B:
            tower_h = sum(subset)
            if result > tower_h:
                result = tower_h


    # 출력: 탑의 높이와 선반의 높이의 차
    sol = result - B
    print(f'#{test_case} {sol}')