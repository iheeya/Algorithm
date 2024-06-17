import sys
from collections import deque

input = sys.stdin.readline

n = int(input())    # n줄의 개수
N = deque([int(input()) for _ in range(n)])    # 만들어야 할 수열

# 하나씩 push된다.
# 스택에 push하는 순서가 오름차순이여야 함
order = deque(sorted(N))   # 스택에 push하는 순서

stack = deque()   # 스택
result = []

for i in range(n):
    num = order.popleft()
    stack.appendleft(num)
    result.append('+')

    for j in range(len(stack)):
        if stack[0] == N[0]:
            stack.popleft()
            N.popleft()
            result.append('-')
        else:
            break


if len(stack) != 0:
    result = ['NO']

for r in result:
    print(r)


