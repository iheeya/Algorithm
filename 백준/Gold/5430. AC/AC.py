import sys
from collections import deque

input = sys.stdin.readline

T = int(input())   # 테스트 케이스의 개수

for tc in range(T):
    P = input().strip()   # 수행할 함수
    n = int(input())   # 배열에 들어 있는 수의 개수
    word = deque(input().rstrip()[1:-1].split(','))

    flag = 1
    R = 0

    if n == 0:
        word = deque()

    for p in P:      
        # 문자열이 존재한다면
        if p == 'R':
            R += 1

        elif p == 'D':
            if word:
                if R % 2 == 0:
                    word.popleft()
                else:
                    word.pop()
            else:
                print('error')
                flag = 0
                break

    
    if flag == 1:
        if R % 2 == 0:
            print('['+",".join(word)+']')
        else:
            word.reverse()
            print('['+",".join(word)+']')


        
    