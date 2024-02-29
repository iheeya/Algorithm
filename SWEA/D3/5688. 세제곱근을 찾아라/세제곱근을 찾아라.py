T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 세제곱 결과가 N이 나오게 되는 수를 구하라

    num = 1      # 세제곱할 수
    result = 0   # 세 제곱근을 저장할 수

    while result < N:
        result = num ** 3
        if result == N:
            break
        num += 1
    else:
        num = -1

    print(f'#{test_case} {num}')
