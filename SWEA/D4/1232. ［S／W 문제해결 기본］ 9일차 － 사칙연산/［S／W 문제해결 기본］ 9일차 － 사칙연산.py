
def postorder(num):
    if num:
        postorder(left[num])
        postorder(right[num])

        if type(tree[num]) == int:
            stack.append(tree[num])
            #어디에 append해야 하는지 똑바로 생각하고 있기!!!
            # 이거 땜에 어이없게 1시간 고민했음..

        else:
            b = stack.pop()
            a = stack.pop()
            if tree[num] == '/':
                stack.append(a // b)
            elif tree[num] == '*':
                stack.append(a * b)
            elif tree[num] == '+':
                stack.append(a + b)
            elif tree[num] == '-':
                stack.append(a - b)




for test_case in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    stack = []

    for i in range(N):
        tmp = input().split()
        if len(tmp) == 4:
            tree[int(tmp[0])] = tmp[1]   # 입력받은 인덱스에 값 저장하기
            left[int(tmp[0])] = int(tmp[2])   # left리스트의 인덱스 == 부모노드 값 / 왼쪽 인덱스값 저장
            right[int(tmp[0])] = int(tmp[3])   # 오른쪽 인덱스값 저장
        else:
            tree[int(tmp[0])] = int(tmp[1])   # tree의 인덱스에 값을 저장

    postorder(1)


    print(f'#{test_case} {stack[-1]}')
