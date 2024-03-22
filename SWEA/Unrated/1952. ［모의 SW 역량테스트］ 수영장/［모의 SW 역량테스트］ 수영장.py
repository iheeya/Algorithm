T = int(input())

for test_case in range(1, T + 1):
    cost = list(map(int, input().split()))  # 일수별 이용권 요금
    # 월과 인덱스 통일
    days = [0] + list(map(int, input().split()))  # 1월부터 12월까지의 이용 계획

    # DP 배열
    plans = [0] * 13

    # 1~12월까지 반복
    for i in range(1, 13):
        # 현재 달의 최소 비용 계산
        # 이전 달 + 1일권 구입 / 이전달 + 한달권 / 3달전 + 3달권 구입 중 최소값 구하기
        # 이전 달 + 1일권 구입 / 이전달 + 한달권 비교 -> 더 작은 값 비교
        plans[i] = min(plans[i-1] + (days[i] * cost[0]), plans[i-1] + cost[1])

        if i >= 3:
            # 3달전 + 3달권 구입과 이전에 저장된 수 비교
            plans[i] = min(plans[i], plans[i -3] + cost[2])

    # 1년권 비교
    min_cost = min(plans[12], cost[3])

    print(f'#{test_case} {min_cost}')