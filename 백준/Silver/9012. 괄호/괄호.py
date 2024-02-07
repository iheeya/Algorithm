T = int(input())

for tc in range(T):
    N = input()
    stack = []

    result = 'YES'    # 결과를 저장하는 변수

    for n in N:
        if n == '(':
            stack.append(n)
        elif n == ')':
            if len(stack) == 0:   # 닫는 괄호인데 stack의 길이가 0이라면
                result = 'NO'
                break
            stack.pop()

    if len(stack) != 0:
        result = 'NO'

    print(result)
