
T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    # 출력: N == x^3 이되는 양의 정수 x , 존재하지 않으면 -1 출력
    
    '''
    N의 제곱근 : N ** (1/2)
    제곱근을 구하기 위해서는 해당 {1/제곱의 수}로 계산할 수 있다.
    '''
    # N의 세제곱근
    num = N ** (1/3)

    # result 반올림,
    result = round(num)

    sol = result ** 3

    if N == sol:
        print(f'#{test_case} {result}')
    # 안되면 -1반환환
    else:
        print(f'#{test_case} -1')