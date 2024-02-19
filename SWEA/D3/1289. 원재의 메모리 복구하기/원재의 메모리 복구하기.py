

T = int(input())

for test_case in range(1, T+1):
    memory = list(map(int, input()))

    fix_num = 0   # 원래 메로리로 복구하기 위해 몇번 고쳐야 하는가

    for i in range(len(memory)):
        if memory[i] == 1 and memory[i-1] == 0:  # 현재 숫자가 1이고 이전 숫자가 0이라면
            fix_num += 1

        elif memory[i] == 0 and memory[i-1] == 1:  # 현재 숫자가 0이고 이전 숫자가 1이라면
            if i == 0:   # 인덱스 i가 0이라면 memory[i-1]이 memory의 마지막 수를 가리키므로
                continue  # 밑의 식들 무시
            fix_num += 1

        elif i == 0 and memory[i] == 1:   # 인덱스가 0이고 값이 1이라면 (시작 숫자가 0이므로)
            fix_num += 1   # 1 증가


    print(f'#{test_case} {fix_num}')
