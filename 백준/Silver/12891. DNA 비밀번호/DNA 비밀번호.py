import sys
input = sys.stdin.readline

S , P = map(int, input().split())    # S: DNA 문자열 길이 P: 사용할 부분 문자열 길이
DNA = input()
lst = list(map(int, input().split()))   # 비밀번호에 꼭 들어가야 할 문자의 최소개수 

check = [0] * 4    # 비밀번호에 포함되어야 할 알파벳의 개수 체크를 위한 리스트
count = 0  # 비빌번호로 쓸 수 있는 부분 문자열의 개수

s = 0  # 스타트 포인터
e = P  # 엔드 포인터

check[0] = DNA[s:e].count('A')
check[1] = DNA[s:e].count('C')
check[2] = DNA[s:e].count('G')
check[3] = DNA[s:e].count('T')

while(True):
    count += 1    # 기본적으로 비빌번호로 쓸 수 있다고 가정
    # 비밀번호로 사용할 수 없을 경우 체크 
    for i in range(4):
        if check[i] < lst[i]:
            count -= 1
            break
    
    #엔드 포인터가 문자열의 길이를 넘으면 while 문 멈춤
    if e >= S:
        break

    # 1. 스타트 포인터 옮기기 (스타트 포인터의 알파벳 삭제하기)
    if DNA[s] == "A":
        check[0] -= 1
    elif DNA[s] == 'C':
        check[1] -=1
    elif DNA[s] == 'G':
        check[2] -= 1
    elif DNA[s] == 'T':
        check[3] -= 1
    
    s +=1   # 스타트 포인터 옮김


    # 2. 엔드 포인터 옮기기 
    # 엔드 포인터의 알파벳 추가
    if DNA[e] == 'A':
        check[0] += 1
    elif DNA[e] =='C':
        check[1] += 1
    elif DNA[e] == 'G':
        check[2] += 1
    elif DNA[e] == 'T':
        check[3] += 1
    
    # 엔드 포인터 옮기기 
    e += 1
    
print(count)