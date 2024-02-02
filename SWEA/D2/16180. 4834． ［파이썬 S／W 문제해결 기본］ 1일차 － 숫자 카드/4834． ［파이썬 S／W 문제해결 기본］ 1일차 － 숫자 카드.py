T = int(input())

for test_case in range(1, T + 1):
    # 0 - 9 숫자가 적힌 N장의 카드
    # 출력 : 가장 많은 카드에 적힌 숫자, 장 수
    # 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.


    N = int(input())
    card = list(map(int, input()))
    count = [0] * 10 # 0 ~ 9까지의 숫자가 적힌 카드들의 개수
    
    c_number = 0   # 가장 많이 적힌 카드 숫자
    mount = 0      # 가장 많이 적힌 숫자 카드 개수
    
    for num in card:
        count[num] +=1     #count 배열에 숫자카드의 갯수만큼 저장 (인덱스: 숫자, 요소: 개수)
        
    for i in range(len(count)):
        if mount <= count[i]:
            mount = count[i]
            c_number = i
            
    print(f'#{test_case} {c_number} {mount}')
      
