import sys
from collections import deque

N = int(sys.stdin.readline())   # 명령의 수

q = deque()   # 명령을 실행할 대상인 스택

for i in range(N):
    command = sys.stdin.readline().split()  # 명령어 입력 (input 값이 있는 경우를 위해 리스트로 입력)

    if command[0] == 'push':
        q.append(command[1])
    
    elif command[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    
    elif command[0] == 'size':
        print(len(q))
    
    elif command[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    
    elif command[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])