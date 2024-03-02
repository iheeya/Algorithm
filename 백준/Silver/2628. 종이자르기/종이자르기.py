w, h = map(int, input().split())   # 종이의 가로, 세로 길이
cut_num = int(input())   # 잘라야 하는 점선의 개수
row = [0, h]    # 가로로 자를 수를 저장할 리스트
col = [0, w]    # 세로로 자를 수를 저장할 리스트

for _ in range(cut_num):
    p, num = map(int, input().split())  # num: 점선번호
    # p == 0: 가로로 자름 , p == 1: 세로로 자름
    
    if p == 0:
        row.append(num)
    else:
        col.append(num)
    
result = 0   # 가장 큰 사각형의 넓이를 저장할 변수
row.sort()
col.sort()

for i in range(len(row)-1):
    for j in range(len(col)-1):
        x = row[i + 1] - row[i]
        y = col[j + 1] - col[j]
        if result < x*y:
            result = x*y

print(result)
        
