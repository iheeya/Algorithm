T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    number = list(input())
    
    my_count = [0] * N
    
    for i in range(len(number)):
        if number[i] == '1':
            my_count[i] = my_count[i-1] + 1
        
        if number[i] == '0':
            my_count [i] = 0
            
    # result = max(my_count)
    
    result = 0
    
    for my in my_count:
        if my > result:
            result = my
        
        
    print(f'#{test_case} {result}')