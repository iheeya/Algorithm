def lotto(dep, idx):
    if dep == 6:
        print(*result)
        return
    
    for i in range(idx, num):
        result.append(arr[i])
        lotto(dep + 1, i + 1)  # 이전에 선택한 숫자를 선택하지 않도록 i+1
        result.pop()
    

while True:
    lst = list(map(int, input().split()))

    if lst[0] == 0:
        break

    arr = lst[1:]
    num = lst[0]
    result = []
    lotto(0, 0)
    print()