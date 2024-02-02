T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a = list(map(int, input().split()))

    # 주어진 숫자에 대해 특별한 정렬한 결과를 10까 까지 출력
    # 가장 큰수, 가장 작은 수 순서대로 쓰기
    result = []

    asc = sorted(a)
    desc = sorted(a, reverse = True)
    # sort는 반환값 없음. a안에서 계산되어 a에 저장된다.

    for i in range(5):
        result.append(desc[i])
        result.append(asc[i])

    print(f'#{test_case}', *result)