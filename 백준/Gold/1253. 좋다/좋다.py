N = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0   # 좋은 수의 개수 

for k in range(N):   # 배열을 앞 부터 배회하면서 좋은 수 구하기
    # 투 포인터 초기화
    i = 0
    j = N - 1
    good = A[k]   # 알고 싶은 수 초기화

    while i < j:
        if A[i] + A[j] < good:
            i += 1
        elif A[i] + A[j] > good:
            j -= 1
        elif A[i] + A[j] == good:
            if i != k and j != k:    # 포인터가 찾고자 하는 수가 아닌지 확인 필요
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1


print(count)

