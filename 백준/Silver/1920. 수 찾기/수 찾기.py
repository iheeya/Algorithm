import sys

N = int(sys.stdin.readline())   # 숫자의 개수
A = list(map(int, sys.stdin.readline().split()))  # 숫자 리스트
A.sort()

M = int(input())  
X = list(map(int, sys.stdin.readline().split()))   # A와 일치하는 숫자가 있는지 확인

# 이진 탐색 사용
for x in X:
    start = 0
    end = N-1
    result = 0   # 결과 값

    while start <= end:
        middle = (start + end) // 2
        if A[middle] == x:
            result = 1
            break

        elif A[middle] < x:   # 중앙값이 더 작다면
            start = middle + 1  # 구간 재설정
        
        elif A[middle] > x: # 중앙값이 더 크다면
            end = middle - 1  

    print(result)  
    

