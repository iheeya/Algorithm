for test_case in range(1, 11):

    l= int(input())
    f = input()    # 계산식 입력 받기
    postfix = ''   # 후위연산자 식을 저장할 문자열
    stack = []     # 후위연산자를 만들기 위한 stack
    cal = []       # 후위연산자 식을 계산할 리스트


    for i in f:    # 입력 받은 식만큼 반복
        if not stack and i == '+':   # 스택에 아무것도 없고 i가 +라면
            stack.append(i)     # 스택에 더하기
        elif stack and i == '+':    # 스택에 값이 있고 i가 +라면 stack안데 숫자가 있다는 것이므로
            postfix += stack.pop()   # postfix에 숫자를 넣고
            stack.append(i)    # +를 스택에 append
        else:    # i가 숫자라면
            postfix += i   # 후위연산자 식에 더하기

    postfix += '+'   # 후위연산자식에 마지막으로 부호 더하기


    for p in postfix:    # 완성된 후위연산자를 반복
        if p != '+':    # p가 + 가 아니라면
            cal.append(p)   # cal에 넣기

        else:   # p가 +라면
            a = cal.pop()   # 두개의 숫자를 꺼내서
            b = cal.pop()
            cal.append(int(a) + int(b))   #더하기 계산이후 다시 리스트에 넣기


    print(f'#{test_case}', *cal)


