T = int(input())

for test_case in range(1, T+1):
    b = input() # 정식이가 기억하는 송금액의 2진수 표현
    t = input()  # 송금액의 3진수 표현
    result = 0   # 송금액을 저장할 변수

    # 2진수와 3진수 각각의 수에서 단 한자리만을 잘못 기억하고 있다.
    stack_1 = list(b)    # 2진수를 리스트로 만들기
    stack_2 = list(t)    # 3진수를 리스트로 만들기


    # 완전 탐색을 이용해 한자리씩 바꾸었을때 일치하는 수가 있다면 해당 수가 송금액
    for i in range(len(b)):   # b의 길이만큼 반복
        stack_2 = list(t)     # 문자열로 입력받은 송금액을 리스트로 바꾸기
        if stack_1[i] == '0':    # 이진수에서 한자리씩 모두 바꿔보기
            tmp = stack_1[i]
            stack_1[i] = '1'
        else:
            stack_1[i] = '0'
        b_str = ''.join(stack_1)   # 바꾼 리스트를 문자열로 변환

        for j in range(len(t)):   # 3진수 바꾸기
            for k in range(3):  #TODO: 3진법이므로 1, 2, 3일때 모두 고려해야한다.
                stack_2[j] = str(k)    # 모든 3진수 고려
                t_str = ''.join(stack_2)   # 바뀐 3진수를 문자열로 변환 
                z = int(b_str, 2)   # 2진수를 10진수로 변환
                g = int(t_str, 3)   # 3진수를 10진수로 변환
                if z == g:     # 만약 2진수와 3진수의 값이 같다면
                    result = z   # 그 값이 정식이가 송금해야할 금액
                    break  # 반복문 멈추기
            stack_2 = list(t)   # 바뀐 3진수를 원래대로 복구
        stack_1 = list(b)   # 바꾼 이진수를 원래대로 복구


    # 출력: 송금할 숫자 출력하기
    print(f'#{test_case} {result}')