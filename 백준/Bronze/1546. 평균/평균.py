N = int(input()) #시험본 과목의 개수

score = list(map(int, input().split()))
M = max(score)

new_score = []

for s in score:
    new_score.append(s/M*100)

n = sum(new_score)
result = n/N


print(result)