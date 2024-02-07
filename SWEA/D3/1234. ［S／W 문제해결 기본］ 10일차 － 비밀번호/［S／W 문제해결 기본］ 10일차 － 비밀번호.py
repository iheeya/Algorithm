for test_case in range(1, 11):
    N, nums = input().split()

    stack = []

    for n in nums:
        if len(stack) == 0:   # 스택안에 아무것도 없다면
            stack.append(n)   # n을 넣기
        elif n == stack[-1]:  # n과 스택의 마지막 요소가 같다면
            stack.pop()    # 스택의 마지막 요소 pop
        else:    # 스택의 마지막 요소와 n이 같지 않다면
            stack.append(n)    #스택에 요소 더하기

    result = ''.join(stack)  # 리스트의 요소를 스트링으로 변환
    print(f'#{test_case} {result}')