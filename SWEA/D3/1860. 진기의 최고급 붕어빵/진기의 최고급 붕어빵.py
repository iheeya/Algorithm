T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    # N: 붕어빵을 살 수 있는 사람들  M: 붕어빵을 만드는데 걸리는 시간  K: 만들 수 있는붕어빵의 개수
    customer = list(map(int, input().split()))   # N명의 손님이 도착하는 시간
    customer.sort()   # 손님이 도착하는 시간을 빠른 순대로 정렬

    sold = 0   # 지금까지 팔린 빵의 개수
    sol = 'Possible'   # 진기가 빵을 팔수 있는지 없는지

    for p in customer:
        make_bread = (p // M) * K

        # 판 빵의 개수
        sold += 1

        # 남은 빵의 개수
        remain = make_bread - sold
        # 남은 빵의 개수가 0보다 작다면 더 이상 손님에게 팔 수 있는 붕어빵이 없다는 것
        if remain < 0:
            sol = 'Impossible'

    print(f'#{test_case} {sol}')

