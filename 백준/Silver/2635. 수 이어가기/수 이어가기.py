N = int(input())   # 처음 주어지는 수
big_nums = []   # 결과를 저장할 리스트

for i in range(1, N+1):  # 두번째 수 구하기
    nums = []   # 값들을 저장할 리스트
    nums.append(N)    # 제일 처음 값 리스트에 넣기
    nums.append(i)    # 반복문의 수 리스트에 넣기
    pp = i     # 이전이전 값
    result = N - i   # 이전값
    p = result
    nums.append(result)
    while True:    # result의 값이 0보다 작지 않을때 까지 반복
        result = pp - p  # 새로운 값 구하기(3번째 값 ~ 끝까지)
        pp = p           # 이전이전 값과 이전값 재정의
        p = result
        if result >=0:    # result 값이 0보다 크거나 같다면
            nums.append(result)   # 숫자 리스트에 넣기
        
        if result <0 :
            break
    
    if len(nums) > len(big_nums):  # 만약 현재 숫자리스트가 기존 리스트보다 크다면
        big_nums = nums    # 바꾸기


print(len(big_nums))
print(*big_nums)
        