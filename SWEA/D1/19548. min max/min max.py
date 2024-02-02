T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T+1):
    N = int(input())  
    a = list(map(int, input().split()))
    
    max = a[0]
    min = a[0]
    
    for number in a:
        if number > max:
            max = number
        if number < min:
            min = number
    
    sol = max - min

    print("#{} {}".format(test_case, sol))