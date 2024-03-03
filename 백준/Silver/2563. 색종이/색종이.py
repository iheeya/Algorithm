T = int(input())   # 색종이의 수
paper = [[0]* 101 for _ in range(101)]   # 도화지의 넓이
cnt = 0  # 색종이의 면적을 저장할 변수

for _ in range(T):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1


for k in range(101):
    for l in range(101):
        if paper[k][l] == 1:
            cnt += 1

print(cnt)