N = int(input())   # 색종이의 장수
arr = [[0]* 1001 for _ in range(1001)]
cnt = 0   # 색종이의 면적을 저장할 변수


for k in range(1, N+1):
    x, y, w, h  = map(int, input().split())
    if x + w < 1001 and y+h <1001:
        for i in range(x, x+w):
            for j in range(y, y+h):
                arr[i][j] = k     # 색종이의 마다 넓이를 각각 다른 수로 채우기

for k in range(1, N+1):
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == k:
                cnt += 1
    
    print(cnt)
    cnt = 0
    
    
    




  