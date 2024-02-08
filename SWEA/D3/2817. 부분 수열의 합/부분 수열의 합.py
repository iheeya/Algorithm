T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    # N: 자연수 수열의 길이
    # K: 찾고자 하는 합
    A = list(map(int, input().split()))   # 수열

    cnt = 0  # N개의 원소를 가지고 있고, 원소의 합이 K인 부분집합의 개수

    for i in range(1 << len(A)):  # 2의 12승개에 해당되는 요소
        subset = []  # 부분집합 원소를 저장할 리스트
        for j in range(len(A)):  # 해당 i의 j번째 비트가 1인지 확인
            if i & (1 << j):  # 비트가 1 이라면 부분집합에 포함되는 요소 (i와 (1<<j)의 & 비트연산의 결과가 참이라면)
                subset.append(A[j])  # 비트가 1 이라면 부분집합 리스트에 append

        if sum(subset) == K:  # 부분집합 원소의 합이 K라면
            cnt += 1  # 부분집합의 개수 1 더하기

        # 중첩 조건문 하나로 쓸 수도 있음
        # if len(subset) == N and sum(subset) == K:
        #     num_subset += 1

    print(f'#{test_case} {cnt}')
