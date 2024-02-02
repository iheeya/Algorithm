T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test = int(input())
    
    #2, 3, 5, 7, 11 소인수분해
    nums = [2, 3, 5, 7, 11]
    count = [0] * 5
    
    for i in range(len(nums)):         # 소인수 분해할 수가 들어 있는 배열의 길이 만큼 반복
        while test % nums[i] == 0:     # 소인수 분해할 수가 들어 있는 배열의 길이 만큼 반복
            count[i] += 1              # 입력받은 수가 0이 아니라면 count 배열 += 1
            test = test // nums[i]           # 소인수분해 할 수 n을 몫으로 바꿔줌
    

    print(f'#{test_case}', end = ' ')
    print(*count)