square = [[0] * 101 for _ in range(101)]
cnt = 0    # 면적을 저장할 변수

for _ in range(4):
    lx, ly, rx, ry = map(int, input().split())

    for i in range(ly, ry):      # 직사각형의 면적에 해당되면 해당 자리를 1로 바꿈
        for j in range(lx, rx):
            square[i][j] = 1

for i in range(101):
    for j in range(101):
        if square[i][j] == 1:     # 해당 자리가 1이라면
            cnt += 1              # cnt +=1 을 통해 면적을 카운팅

print(cnt)