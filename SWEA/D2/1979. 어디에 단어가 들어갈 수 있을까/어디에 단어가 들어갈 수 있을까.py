T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())   # N: 퍼즐의 가로세로 길이  K: 단어의 길이
    
    puzzle = [list(map(int, input().split())) for _ in range(N)]   #퍼즐의 모양 흰색:1 검은색:0
    #흰색 부분에 단어가 가로, 세로로 들어갈 수 있다.
    
    # K길이를 갖는 단어가 들어갈수 있는 자리는 몇개인지 출력
    
    # 하나의 행렬에 가로, 세로 모두 확인 -> 길이를 리스트에 저장
    result = 0
    
    for row in range(N):     #가로 칸에 들어갈 수 있는 단어
        count = 0 
        for col in range(N):
            if puzzle[row][col] == 1:
                count += 1
            if puzzle[row][col] == 0 or col == N-1:
                if count == K:
                    result += 1
                if puzzle[row][col] == 0:
                    count = 0
                    
         
    #세로 칸에 들어갈 수 있는 단어
    for row in range(N):
        count = 0
        for col in range(N):
            if puzzle[col][row] == 1:
                count += 1
            if puzzle[col][row] == 0 or col == N-1:
                if count == K:
                    result += 1
                if puzzle[col][row] == 0:
                    count = 0
    
     
    
    print(f'#{test_case} {result}')     