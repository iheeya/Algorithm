A, P = map(int, input().split())

def next_num(x):
    return sum(int(d) ** P for d in str(x))  # int(d)로 변환하고 결과를 return

visited = [0] * (354296)
cnt = 0

def dfs(A):
    global cnt
    nx = next_num(A)

    cnt += 1
    visited[A] += 1

    if visited[nx] == 3:
        return 0

    if visited[A] == 2:
        cnt -= 3
 

    if visited[nx] <= 2:
        dfs(nx)
    
    

dfs(A)
print(cnt)
