tc = []

for i in range(28):
    N = int(input())
    tc.append(N)  #입력받은 N을 배열에 추가

result = []  # 과제를 제출하지 않은 출석번호를 저장할 배열

for i in range(1, 31):
    if i not in tc:
        result.append(i)

result.sort  # result 배열의 출석번호 정렬

for i in range(len(result)):
    print(result[i])