N = int(input())
M = int(input())
A = list(map(int, input().split()))

A.sort()  # 오름차순으로 정렬
# 투포인터 지정
i = 0
j = N -1
count = 0    # 만들 수 있는 갑옷의 개수 카운트트

while i < j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    elif A[i] + A[j] == M:
        i += 1
        j -= 1
        count += 1

print(count)