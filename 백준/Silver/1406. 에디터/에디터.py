import sys
from collections import deque

input = sys.stdin.readline

left = deque(input().strip())
right = deque()
M = int(input().strip())  # 명령어의 개수

for _ in range(M):
    cmd = input().split()

    if cmd[0] == 'L' and left:
        right.appendleft(left.pop())
    elif cmd[0] == 'D' and right:
        left.append(right.popleft())
    elif cmd[0] == 'B' and left:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

print(''.join(left) + ''.join(right))
