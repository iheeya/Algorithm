T = int(input())

for test_case in range(1, T+1):
    A, B = input().split()

    cnt = A.count(B)   # A문자열에 B문자열이 있는 수 반환
    result = len(A) - cnt*(len(B)-1)

    print(f'#{test_case} {result}')