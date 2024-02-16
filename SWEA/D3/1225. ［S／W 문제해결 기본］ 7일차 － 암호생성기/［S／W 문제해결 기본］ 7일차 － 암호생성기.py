for test_case in range(1, 11):
    num = int(input())   # 테스트 케이스의 번호
    q = list(map(int, input().split()))

    minus = 1


    # 큐에 저장된 숫자가 한자리수가 될때 까지 반복 (마지막 암호 배열은 모두 한 자리 수로 구성되어 있다.)
    while True:
        if minus > 5:  # 5까지 증가하며 감소하기 때문에 뺄 숫자가 5가 넘어간다면
            minus = 1  # 뺄 값을 1로 초기화

        # 순회하며 5까지 뺀다
        x = q.pop(0) - minus
        
        # 큐에 저장된  숫자가 0이거나 0 이하라면 반복 중단
        if x <= 0:
            q.append(0)
            break

        q.append(x)  # 0보다 크다면 q에 다시 append
        minus += 1   # 뺄 값을 1w증가


    print(f'#{num}', *q)