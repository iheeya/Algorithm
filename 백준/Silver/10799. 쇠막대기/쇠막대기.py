
tc = input()

stack = []    # 막대의 개수를 세기 위한 stack
cnt = 0   # 잘린 막대기의 개수를 세기 위한 변수

for i in range(len(tc)):
    # 1. 만약 문자가 (이라면 stack에 append
    if tc[i] == '(':
        stack.append('(')

    if tc[i] == ')':     # 닿는 괄호라면
        if tc[i-1] == '(':     # 이전 문자가 여는 괄호라면 레이저인 것이므로
            stack.pop()        # pop()한다
            cnt += len(stack)  # 쇠막대기 개수에 스택의 길이만큼 더한다.

        else:      # 레이저가 아니라면
            cnt += 1      # 쇠막대기 하나가 끝난 것이므로 1을 더함
            stack.pop()   # 쇠막대기 하나의 시작을 제거


print(cnt)
    