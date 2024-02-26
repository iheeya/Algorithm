def calc_cnt(N):
    cnt = 0
    for i in range(-N, N+1):  # 원의 지름의 범위
        for j in range(-N, N+ 1):
            ans = i**2 + j ** 2
            if ans <= N**2:    # 격자점을 구하기 위한 식을 만족한다면
                cnt += 1

    return cnt


T = int(input())

for test_case in range(1, T+1):
    N = int(input())   # 반지름의 길이

    print(f'#{test_case} {calc_cnt(N)}')