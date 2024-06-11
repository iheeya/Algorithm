import sys
from collections import deque

input = sys.stdin.readline
dq = deque()

N = int(input())   # 명령어의 개수

for _ in range(N):
    cmd = list(input().split())   # 명령어 입력

    if cmd[0] == 'push_front':
        dq.appendleft(cmd[1])
    
    elif cmd[0] == 'push_back':
        dq.append(cmd[1])
    
    elif cmd[0] == 'pop_front':
        if len(dq) !=0:
            print(dq.popleft())
        else:
            print(-1)

    elif cmd[0] == 'pop_back':
        if len(dq) != 0:
            print(dq.pop())
        else:
            print(-1)
    
    elif cmd[0] == 'size':
        print(len(dq))
    
    elif cmd[0] == 'empty':
        if len(dq) != 0:
            print(0)
        else:
            print(1)
    
    elif cmd[0] == 'front':
        if len(dq) !=0:
            print(dq[0])
        else:
            print(-1)
    
    elif cmd[0] == 'back':
        if len(dq) !=0:
            print(dq[-1])
        else:
            print(-1)