T = int(input())

for test_case in range(1, T+1):
    days = int(input())   # 원재가 매매가를 알고 있는 날의 수

    prices = list(map(int, input().split()))   # 매매가들의 모음
    stack = []
    result = []   #이익을 저장할 리스트


    for p in prices[::-1]:    # 역순으로 순회
        if len(stack) == 0:   # 리스트에 값이 없다면
            stack.append(p)   # 가격 append
        elif p > stack[-1]:   # 현재 가격이 스택의 마지막 가격보다 크다면
            stack.append(p)   # 이익을 내고 팔 수 없으므로 스택에 추가
        elif p < stack[-1]:   # 현재 가격이 스택의 마지막 가격보다 작다면
            result.append(stack[-1] - p)    # 이익을 낼 수 있으므로 이익을 result 리스트에 저장

    if len(stack) == days:    # 만약 스택의 길이가 매매가를 알고 있는 날보다 크다면
        sol = 0               # 팔 수 있는 날이 없는 것이므로 이익은 0
    else:
        sol = sum(result)    # 이익의 합 계산

    print(f'#{test_case} {sol}')
