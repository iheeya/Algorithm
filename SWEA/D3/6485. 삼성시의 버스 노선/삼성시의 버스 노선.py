
T = int(input())

for test_case in range(1, T+1):
    N = int(input())   # 버스 노선의 수

    # 출력: P개의 버스 정류장에 대해 각 정류장에 몇개의 버스 노선이 다니는가?
    result = []  # 결과를 저장할 리스트
    bus_stop = [0] * 50001  # 인덱스 번호 == 버스 정류장번호 (1 ~5000)

    for i in range(N):
        A, B = map(int, input().split())  # A이상, B이하인 버스정류장만을 다니는 버스 노선
        for j in range(A, B+1):
            bus_stop[j] += 1

    P = int(input())  # 버스 정류장의 수
    for i in range(P):
        C = int(input())
        result.append(bus_stop[C])
    
    print(f'#{test_case}', *result)