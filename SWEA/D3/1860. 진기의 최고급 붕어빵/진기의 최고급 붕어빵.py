T = int(input())

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    # N: 붕어빵을 살 수 있는 사람
    # M: 진기가 붕어빵을 만드는 시간  (M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.)
    # K: 만든 붕어빵의 개수
    nums = list(map(int, input().split()))   # 사람들이 언제 도착하는지 나타내는 초 단위(한 사람씩 따로 온다.)

    result = 'Possible'   # 진기가 손님을 기다리게 하지 않고 붕어빵을 줄지 안줄지

    # 손님이 오는 시간 순대로 정렬
    nums.sort()

    # 진기가 n초 안에 만들 수 있는 붕어빵의 개수보다 손님이 오는 시간이 더 빠르다면 불가능
    for i in range(N):   # 붕어빵을 살 수 있는 사람의 수 만큼 반복
        b = (nums[i]//M) * K  # nums[i]초 까지 만들 수 있는 붕어빵의 개수
        if b < i+1:  # 붕어빵의 개수가 손님의 수보다 작으면
            result = 'Impossible'  # 붕어빵을 줄 수 없다.

    print(f'#{test_case} {result}')