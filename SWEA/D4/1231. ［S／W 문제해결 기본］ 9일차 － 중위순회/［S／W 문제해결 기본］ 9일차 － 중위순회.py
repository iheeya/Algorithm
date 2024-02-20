def inorder(n):
        global result

        if n <= N:   # 현재 노드의 수가 마지막 노드의 수와 같거나 작으면
            inorder(n*2)   # 왼쪽 자식 노드
              
            result.append(tree[n])   # 트리의 n번인덱스의 요소를 result에 append -> 중위순회 결과 n번 노드의 차례가 되면

            inorder((n*2)+1)   # 오른쪽 자식 노드


for test_case in range(1, 11):
    N = int(input())   # 트리가 갖는 정점의 총 수
    tree = [False]*(N+1)  # 노드의 번호 == 인덱스로 갖도록 
    result = []   # 순회 결과를 저장할 리스트

    info = [list(input().split()) for _ in range(N)]   # 노드번호와 문자 입력받기

    for i in range(N):   # 노드의 길이만큼 반복
         tree[i+1] = info[i][1]   # 해당 노드에 맞는 문자열을 넣음

    
    inorder(1)   # 루트 노드부터 중위순회 시작
    sol = ''.join(result)   # 리스트에서 공백 없애기

    print(f'#{test_case}', sol)


    