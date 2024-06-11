N = int(input())   # 상근이가 가지고 있는 숫자 카드의 개수
N_lst = list(map(int, input().split()))
N_lst.sort()

M = int(input())
M_lst = list(map(int, input().split()))

result = 0   # 결과물

# 이진탐색 사용
for m in M_lst:
    start = 0
    end = N - 1
    result = 0

    while start <= end:
        middle = (start + end) // 2
        
        if N_lst[middle] == m:
            result = 1
            break

        elif N_lst[middle] < m:
            start = middle + 1
        
        elif N_lst[middle] > m:
            end = middle -1
    
    print(result, end = ' ')

