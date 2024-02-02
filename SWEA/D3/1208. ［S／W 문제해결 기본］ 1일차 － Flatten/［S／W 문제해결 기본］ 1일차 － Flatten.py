for test_case in range(1, 11):
    dumps = int(input())    #덤프 횟수
    box_height = list(map(int, input().split()))    # 각 상자의 높이 값
    
    for i in range(dumps):
        max_value = max(box_height) 
        min_value = min(box_height) 
        
        max_idx = box_height.index(max_value)
        min_idx = box_height.index(min_value)
        
        box_height[max_idx] -= 1
        box_height[min_idx] += 1
        
        if max(box_height) - min(box_height) <= 1:
            break
        
        
    result = max(box_height) - min(box_height)    
    
    print(f'#{test_case} {result}')
        
