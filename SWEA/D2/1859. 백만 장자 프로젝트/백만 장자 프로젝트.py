
T = int(input())

for test_case in range(1, T+1):
    N = int(input())    # 원재가 알고 있는 날짜 수
    price = list(map(int, input().split()))    # N일 동안의 물건 값
    n_price = price[::-1]

    cnt = 0  # 이익이 난 가격
    stack = []

    for n in n_price:
        if len(stack) == 0:
            stack.append(n)
        if stack[-1] < n:   # 스택에 저장된 값보다 지금 값이 크다면
            stack.pop()     # 스택에 저장된 값 pop
            stack.append(n)  # 새로운 가격 append
        else:
            cnt += (stack[-1] - n)

    print(f'#{test_case} {cnt}')



