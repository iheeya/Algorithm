import sys
input = sys.stdin.readline

N, M = map(int, input().split())   # N: 강의 개수, M: 블루레이 개수
lecs = list(map(int, input().split())) # 각 강의의 길이

start = max(lecs)  # 블루레이의 최소 크기
end = sum(lecs)    # 블루레이의 최대 크기
result = end        # 정답


while start <= end:
    mid = (start + end) // 2
    cnt = 1  # 블루레이 개수
    total=0   # 강의 시간 합

    for lec in lecs:
        if total + lec > mid:
            cnt += 1
            total =0
        total += lec
        
    if cnt <= M:   # 블루레이 개수를 예정 보다 적게 사용했다면
        result = mid
        end = mid - 1
    
    else:
        start = mid + 1


print(result)


