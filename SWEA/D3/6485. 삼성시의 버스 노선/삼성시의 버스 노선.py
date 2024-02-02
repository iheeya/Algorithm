T = int(input())   #테스트 케이스

for test_case in range(1, T+1):
    bus_stops = [0] * 5001    # 삼성시의 버스 정류장 번호

    N = int(input())   # 버스 노선 N개

    for stops in range(N):
        A, B = map(int, input().split())
        for stop in range(A, B+1):
            bus_stops[stop] += 1

    P = int(input())
    result = []

    for c in range(P):
        C = int(input())
        result.append(bus_stops[C])

    print(f'#{test_case}', *result)