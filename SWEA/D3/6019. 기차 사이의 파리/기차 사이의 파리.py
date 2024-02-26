T = int(input())

for test_case in range(1, T+1):
    D, A, B, F = map(int, input().split())
    # D: 두 기차 전면부 사이의 거리, A: 기차 A의 속력, B: 기차 B의 속력, F: 파리의 속력

    # 거리 = 시간 * 속력
    fly = (D * F) / (A + B)   # 파리가 움직인 거리

    print(f'#{test_case} {fly:.10f}')