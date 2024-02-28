T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())   # N: 수열의 개수 K: 구하고자 하는 합
    A = list(map(int, input().split()))    # N개의 자연수 수열
    cnt = 0  # 합이 K인 부분집합의 개수를 저장할 변수


    # 비트연산자를 이용해 부분집합 만들기
    for i in range(1<<N):
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(A[j])
        if sum(subset) == K:  # 부분집합의 원소들의 합이 K라면 cnt += 1
            cnt += 1

    # 출력: 합이 K가 되는 경우의 수
    print(f'#{test_case} {cnt}')