S = list(input().split())

cnt = 0   # 문자의 개수를 저장할 변수

for i in range(len(S)):
    if S[i] == ' ':
        S.pop(i)
    else:
        cnt += 1

print(cnt)
    

