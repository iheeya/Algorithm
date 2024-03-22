# [Unrated] [모의 SW 역량테스트] 수영장 - 1952 

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq) 

### 성능 요약

메모리: 47,772 KB, 시간: 103 ms, 코드길이: 813 Bytes

### 제출 일자

2024-03-22 11:12



> 출처: SW Expert Academy, https://swexpertacademy.com/main/code/problem/problemList.do

# 다른 풀이방법 
## 완전탐색으로 풀이
```python
# 완전 탐색
def dfs(month, sum_cost):
    global ans
    # 기저조건:
    # 1. 12월까지 모두 봤으면 종료
    if month > 12:
        # 최소비용
        ans = min(ans, sum_cost)
        return
    # 2. 이미 최솟값을 넘어가면 종료
    if sum_cost > ans:
        return

    # 모두 1일권으로 구매
    dfs(month + 1, sum_cost + (days[month] * cost[0]))

    # 1달권 구매
    dfs(month + 1, sum_cost + cost[1])

    # 3달권 구매
    dfs(month + 3, sum_cost + cost[2])

    # 1년권 구매
    dfs(month + 12, sum_cost + cost[3])


T = int(input())

for test_case in range(1, T + 1):
    cost = list(map(int, input().split()))  # 일수별 이용권 요금
    # 월과 인덱스 통일
    days = [0] + list(map(int, input().split()))  # 1월부터 12월까지의 이용 계획
    ans = int(1e9)

    dfs(1, 0)
    print(f'#{test_case} {ans}')

```
