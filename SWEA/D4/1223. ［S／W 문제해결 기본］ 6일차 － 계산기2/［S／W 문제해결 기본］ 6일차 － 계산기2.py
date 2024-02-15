

for test_case in range(1, 11):
    # 문자열 길이 N
    N = int(input())
    # 문자열 계산식
    infix = input().rstrip()

    stack = []   # 후위연산자를 만들때 사용할 스택 (연산자만 push)
    postfix = ''  # 후위연산자식
    cal = []  # 후위연산자를 계산할때 사용할 스택

    for ch in infix:
        if ch.isdigit():   # ch가 숫자라면 postfix에 넣기
            postfix += ch

        elif ch == '*':   # ch가 곱하기 문자라면
            if len(stack) > 0 and (stack[-1] == '*'):  # stack의 마지막 요소가 *라면
                postfix += stack.pop()   # stack의 마지막 요소를 postfix에 더하기
            stack.append(ch)   # * 연산자를 stack에 append

        elif ch == '+':   # ch가 더하기 문자라면
            while len(stack) > 0:     # stack이 비지 않았고 스택의 마지막 요소가 * 가 아니라면
                postfix += stack.pop()   # stack의 마지막 요소를 postfix에 더하기
            stack.append(ch)    # + 연산자를 stack에 append

    while len(stack) > 0:
        postfix += stack.pop()

    # print(postfix)

    for ch in postfix:
        if ch.isdigit():   # ch가 숫자라면
            cal.append(ch)   # 계산을 위한 리스트 cal 에 추가

        elif ch == '*':   # ch가 곱하기라면
            b = int(cal.pop())   # 마지막으로 cal에 삽입한 숫자를 두개 꺼냄
            a = int(cal.pop())
            sol = cal.append(a*b)   # 계산한 결과를 다시 cal리스트에 삽입

        elif ch == '+':    # ch가 더하기라면
            b = int(cal.pop())    # 마지막으로 cal에 삽입한 숫자 두개 꺼냄
            a = int(cal.pop())
            sol = cal.append(a + b)   #계산한 결과를 다시 cal에 삽입

    # cal리스트에는 후위연산자식을 계산한 결과가 저장되게 된다.
    print(f'#{test_case}', *cal)




