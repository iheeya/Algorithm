N = int(input())
lst = []

for i in range(1, N+1):
    cnt = 0
    for ch in str(i):
        if ch in '369':
            cnt += 1

    if cnt == 1:
        lst.append('-')
    elif cnt == 0:
        lst.append(i)
    else:
        lst.append('-' * cnt)


print(*lst)